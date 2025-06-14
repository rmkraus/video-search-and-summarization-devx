from pathlib import Path
import requests
from typing import Literal, Any
from urllib.parse import urljoin

def check_response(response):
    """Return the proper response."""
    response.raise_for_status()
    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        return response.text

def vss_api_call(
        vss_url: str,
        target: str,
        params: None | dict[str, str] = None,
        verb: Literal["get"] | Literal ["post"] = "get",
        json: Any = None,
        files: Any = None,
        data: Any = None,
    ) -> dict[str, Any] | str:
    """Query the VIA Agent API and handle the response."""
    # determine the full url
    url = urljoin(vss_url, target)

    # query the api
    if verb == "get":
        response = requests.get(url, params=params)
    elif verb == "post":
        response = requests.post(url, params=params, json=json, data=data, files=files)
    else:
        raise ValueError("Verb must be either get or post.")

    return check_response(response)

class Chat:
    """A simple wrapper to chat with a video."""

    def __init__(self, vss_url: str, video_id: str, model_id: str):
        """Initialize the class."""
        self.vss_url = vss_url
        self.video_id = video_id
        self.model_id = model_id

    def query(self, msg: str):
        """Chat with the VSS agent."""
        # format the message
        messages = [{
            "content": msg,
            "role": "user"
        }]

        # generate request payload
        payload = {
            "id": self.video_id,
            "messages": messages,
            "model": self.model_id,
        }

        # query the vss agent
        response_data = vss_api_call(
            self.vss_url,
            "chat/completions",
            verb="post",
            json=payload
        )
        answer = response_data["choices"][0]["message"]["content"]

        return answer