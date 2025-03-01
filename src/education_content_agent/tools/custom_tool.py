from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from duckduckgo_search import DDGS
import requests
from markdownify import markdownify
import re

class DuckDuckGoSearchToolInput(BaseModel):
    """Input schema for DuckDuckGoSearchTool."""
    query: str = Field(..., description="The search query to perform.")
    
class DuckDuckGoSearchTool(BaseTool):
    name: str = "web_search"
    description: str = (
        "Performs a DuckDuckGo web search based on your query, then returns the top search results."
    )
    args_schema: Type[BaseModel] = DuckDuckGoSearchToolInput
    
    def _run(self, query: str) -> str:
        ddgs = DDGS()
        results = ddgs.text(query, max_results=10)
        if not results:
            raise Exception("No results found! Try a less restrictive/shorter query.")
        postprocessed_results = [f"[{result['title']}]({result['href']})\n{result['body']}" for result in results]
        return "## Search Results\n\n" + "\n\n".join(postprocessed_results)


class VisitWebpageToolInput(BaseModel):
    """Input schema for VisitWebpageTool."""
    url: str = Field(..., description="The URL of the webpage to visit.")

class VisitWebpageTool(BaseTool):
    name: str = "visit_webpage"
    description: str = (
        "Visits a webpage at the given URL and reads its content as a markdown string. Use this to browse webpages."
    )
    args_schema: Type[BaseModel] = VisitWebpageToolInput

    def _run(self, url: str) -> str:
        try:
            response = requests.get(url, timeout=20)
            response.raise_for_status()
            markdown_content = markdownify(response.text).strip()
            markdown_content = re.sub(r"\n{3,}", "\n\n", markdown_content)
            return markdown_content[:10000]  # Truncate content if too long
        except requests.exceptions.Timeout:
            return "The request timed out. Please try again later or check the URL."
        except requests.exceptions.RequestException as e:
            return f"Error fetching the webpage: {str(e)}"
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"