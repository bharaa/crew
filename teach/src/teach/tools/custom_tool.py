from typing import Type
from crewai_tools import BaseTool
from pydantic import BaseModel, Field
import requests
import json
import os
from dotenv import load_dotenv
class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class serperTool(BaseTool):
    name: str = "custom serper dev tool"
    description: str = (
        "search the internet for latest news"
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # Implementation goes here
        url = "https://google.serper.dev/news"

        payload = json.dumps({
        "q": argument,
        "location": "India",
        "gl": "in",
        "tbs": "qdr:d"
        })
        headers = {
        'X-API-KEY': os.getenv("SERPER_API_KEY"),
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        response_data = response.json()

        news_data = response_data.get('news',[])

        return json.dumps(news_data, indent=2)
