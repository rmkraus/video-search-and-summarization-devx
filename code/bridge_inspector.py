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
    ...


def upload_video_to_vss(vss_url: str, file_path: str):
    """Upload a video file to to the VSS API.
    
    Inputs:
      vss_url: [str] The HTTP URL to the VSS API
      file_path: [str] The path to a video file.

    Returns: [str] The id for the uploaded video.
    """
    ...


def summarize_video(vss_url: str, video_id: str, model_id: str):
    """Generate a summary of a bridge inspection video.
    
    Inputs:
      vss_url: [str] The HTTP URL to the VSS API
      video_id: [str] The id for the uploaded video file.
      model_id: [str] The name of the VLM to use.
      
    Returns: [str] The generated summary.
    """
    ...


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
def main(video_files: list[str], vss_url: str):
    """Run the bridge inspection pipeline."""
    # get the first model name
    model_id = ...
    
    for video in video_files:
        # upload the video
        print(f"Uploading video: {video}")
        video_id = ...

        # summarize the video
        print(f"Generating summary for {video_id} using {model_id}")
        report = ...

        # connect to the chat server
        chat_client = ...

        # wait for the database to be ready
        # TODO: this will be replaced with an official check
        print("Waiting for database to be ready.")
        while chat_client.query("Are you ready?") == "Sorry, I don't see that in the video.":
            print("Waiting 30 seconds...")
            time.sleep(30)

        # ask follow up questions
        print("Asking for more information.")
        escalations = ...
        priority = ...
        title = ...
        emergencies = ...

        # write a report on the bridge's condition
        print("Write the final report:\n")
        print("="*80 + "\n\n")
        write_report(title, priority, emergencies, escalations, report)
        

if __name__ == "__main__":
    # run our custom pipeline
    main()
