import os

from serpapi import GoogleSearch
from dotenv import load_dotenv

load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_KEY")


def build_query(base_query, domains):

    if not domains:
        return base_query

    domain_filters = " OR ".join(
        [f"site:{d}" for d in domains]
    )

    return f"{base_query} ({domain_filters})"


def search_agent(
    query: str,
    max_results: int = 5,
    trusted_domains=None
):

    if trusted_domains is None:
        trusted_domains = []

    final_query = build_query(
        query,
        trusted_domains
    )

    params = {
        "engine": "google",
        "q": final_query,
        "api_key": SERPAPI_KEY,
        "num": max_results
    }

    try:

        search = GoogleSearch(params)

        results = search.get_dict()

        organic_results = results.get(
            "organic_results",
            []
        )

        parsed_results = []

        for r in organic_results:

            parsed_results.append({
                "title": r.get("title"),
                "url": r.get("link"),
                "snippet": r.get("snippet")
            })

        return {
            "query_used": final_query,
            "results": parsed_results
        }

    except Exception as e:

        return {
            "error": str(e),
            "results": []
        }