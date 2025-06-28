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
    ...  # TODO


def upload_video_to_vss(vss_url: str, file_path: str):
    """Upload a video file to the VSS API.
    
    Inputs:
      vss_url: [str] The HTTP URL to the VSS API
      file_path: [str] The path to a video file.

    Returns: [str] The id for the uploaded video.
    """
    ...  # TODO


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
            "prompt": ...,  # TODO
            "caption_summarization_prompt": ...,  # TODO
            "summary_aggregation_prompt": ...,  # TODO
            "model": model_id,
            "max_tokens": 1024,
            "temperature": 0.9,
            "top_p": 0.9,
            "num_frames_per_chunk": 5,
            "chunk_duration": 35,
            "chunk_overlap_duration":5,
            "enable_chat": True,
    }

    # send to vss server
    summarize_response = ...  # TODO
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
    model_id = ...  # TODO
    
    for video in video_files:
        # upload the video
        print(f"Uploading video: {video}")
        video_id = ...  # TODO
        
        # summarize the video
        print(f"Generating summary for {video_id} using {model_id}")
        report = ...  # TODO

        # connect to the chat server
        chat_client = ...  # TODO

        # ask follow up questions
        print("Asking for more information.")
        title = "Bridge Inspection"
        escalations = ...  # TODO
        priority = ...  # TODO
        emergencies = ...  # TODO

        # write a report on the bridge's condition
        print("Write the final report:")
        print()
        print()
        write_report(title, priority, emergencies, escalations, report)
        

if __name__ == "__main__":
    # run our custom pipeline
    pipeline()