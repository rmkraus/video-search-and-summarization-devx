#!/usr/bin/env python3
"""Automatic Visual Bridge Inspection."""

import sys
from pathlib import Path
from typing import Literal, Any
import time

import click

from helpers import check_response, vss_api_call, Chat


def lookup_model_id(vss_url: str):
    """Lookup the id for the first available VLM model.

    Inputs:
      vss_url: [str] The HTTP URL to the VSS API

    Returns: [str] The ID of the first model
    """
    models_response = vss_api_call(vss_url, "models")
    return models_response["data"][0]["id"]


def upload_video_to_vss(vss_url: str, file_path: str):
    """Upload a video file to to the VSS API.
    
    Inputs:
      vss_url: [str] The HTTP URL to the VSS API
      file_path: [str] The path to a video file.

    Returns: [str] The id for the uploaded video.
    """
    video = Path(file_path)
    
    with video.open("rb") as file:
        # setup query data
        files = {"file": (video.name, file)}
        data = {"purpose":"vision", "media_type":"video"}
    
        # query the vss api
        upload_response = vss_api_call(
            vss_url,
            "files",
            verb="post",
            files=files,
            data=data
        )

    return upload_response["id"]


def summarize_video(vss_url: str, video_id: str, model_id: str):
    """Generate a summary of a bridge inspection video.
    
    Inputs:
      vss_url: [str] The HTTP URL to the VSS API
      video_id: [str] The id for the uploaded video file.
      model_id: [str] The name of the VLM to use.
      
    Returns: [str] The generated summary.
    """
    # create the request body
    body = {
            "id": video_id,
            "prompt": "You are a bridge inspector. Describe any concerns you have with this bridge in detail. Your concerns may be: cosmetic, structural, landscaping, or vandalism in nature.Start each event description with a start and end time stamp of the event.",
            "caption_summarization_prompt": "If any descriptions have the same meaning and are sequential then combine them under one sentence and merge the time stamps to a range. Format the timestamps as 'mm:ss'",
            "summary_aggregation_prompt": "Based on the available information, generate a report that describes the condition of the bridge. The report should be organized into cosemetic, structual, vegetation overgrowth, and vandalism. The report must include timestamps. This should be a concise, yet descriptive summary of all the important events. The format should be intuitive and easy for a user to understand what happened. Format the output in Markdown so it can be displayed nicely.",
            "model": model_id,
            "max_tokens": 1024,
            "temperature": 0.9,
            "top_p": 0.9,
            "num_frames_per_chunk": 15,
            "chunk_duration": 35,
            "chunk_overlap_duration":5,
            "enable_chat": True,
    }

    # send the to vss server
    summarize_response = vss_api_call(vss_url, "summarize", verb="post", json=body)
    return summarize_response["choices"][0]["message"]["content"]


def write_report(title: str, priority: str, emergencies: str, escalations: str, report: str):
    """Write the full report in markdown."""
    sys.stdout.write(f"# {title}\n{priority}\n\n")
    sys.stdout.write(f"## Urgent Actions\n{emergencies}\n\n")
    sys.stdout.write(f"## Remediations Needed\n{escalations}\n\n")
    sys.stdout.write(f"## Bridge Condition\n{report}\n\n")
    

@click.command()
@click.argument('video_files', type=click.Path(exists=True), nargs=-1)
@click.option('--vss-url', envvar='VSS_URL', default="http://via-server:8100",
              help="URL to the VIA Server API")
def pipeline(video_files: list[str], vss_url: str):
    """Run the bridge inspection pipeline."""
    # get the first model name
    model_id = lookup_model_id(vss_url)
    
    for video in video_files:
        # upload the video
        print(f"Uploading video: {video}")
        video_id = upload_video_to_vss(vss_url, video)

        # summarize the video
        print(f"Generating summary for {video_id} using {model_id}")
        report = summarize_video(vss_url, video_id, model_id)

        # connect to the chat server
        chat_client = Chat(
            vss_url, 
            video_id=video_id,
            model_id=model_id,
        )

        # wait for the database to be ready
        print("Waiting for database to be ready.")
        while chat_client.query("Are you ready?") == "Sorry, I don't see that in the video.":
            print("Waiting 30 seconds...")
            time.sleep(30)

        # ask follow up questions
        print("Asking for more information.")
        escalations = chat_client.query("List any necessary escelations for maintenance.")
        priority = chat_client.query("Score the priority of this report.")
        title = chat_client.query("Create a title for this report.")
        emergencies = chat_client.query("Does this the bridge require immediate structural attention?")

        # write a report on the bridge's condition
        print("Write the final report:")
        print()
        print()
        write_report(title, priority, emergencies, escalations, report)
        

if __name__ == "__main__":
    # run our custom pipeline
    pipeline()