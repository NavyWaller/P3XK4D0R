import os

from serpapi import GoogleSearch
from dotenv import load_dotenv

load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_KEY")


def search_agent(query: str, max_results: int = 5):

    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_KEY,
        "num": max_results
    }

    try:

        search = GoogleSearch(params)

        results = search.get_dict()

        organic_results = results.get("organic_results", [])

        parsed_results = []

        for r in organic_results:

            parsed_results.append({
                "title": r.get("title"),
                "url": r.get("link"),
                "snippet": r.get("snippet")
            })

        return {
            "results": parsed_results
        }

    except Exception as e:

        return {
            "error": str(e),
            "results": []
        }