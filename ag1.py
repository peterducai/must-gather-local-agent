# pip install -qU langchain langchain-ollama
from langchain.agents import create_agent


#   model="ollama:qwen3.6:27b",

import requests
from langchain.tools import tool
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent


@tool
def fetch_url(url: str) -> str:
    """Fetch text content from a URL"""
    response = requests.get(url, timeout=10.0)
    response.raise_for_status()
    return response.text

system_prompt = """\
Use fetch_url when you need to fetch information from redhat.com; quote relevant snippets.
"""

agent = create_agent(
    model="ollama:qwen3.6:27b",
    tools=[fetch_url], # A tool for retrieval
    system_prompt=system_prompt,
)