from typing import Literal, Optional
from langchain.tools import tool 
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os 
from dotenv import load_dotenv
from rich import print
load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(
    query: str,
    time_range: Optional[Literal["day", "week", "month", "year"]] = None,
) -> str:
    """Search the web for recent and reliable information on a topic. Optionally pass time_range ('day', 'week', 'month', or 'year') to filter for recent results. Returns Titles, URLs, Published dates (if available), and snippets."""
    search_kwargs = {"query": query, "max_results": 5}
    if time_range:
        search_kwargs["time_range"] = time_range
    results = tavily.search(**search_kwargs)

    out = []

    for r in results['results']:
        published = r.get("published_date")
        pub_line = f"Published: {published}\n" if published else ""
        out.append(
            f"Title: {r['title']}\nURL: {r['url']}\n{pub_line}Snippet: {r['content'][:300]}\n"
        )
    
    return "\n----\n".join(out)

@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""
    try:
        resp = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)[:3000]
    except Exception as e:
        return f"Could not scrape URL: {str(e)}"