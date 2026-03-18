import os

from ddgs import DDGS

from config import settings


def write_report(filename: str, content: str) -> str:
    path = "./" + settings.output_dir + "/" + filename

    dirpath = os.path.dirname(path) or "."
    os.makedirs(dirpath, exist_ok=True)

    with open(path, 'w', encoding="utf-8") as f:
        f.write(content)

    return f"Report written to {path}"


def web_search(query: str) -> list[dict]:
    try:
        search_results = DDGS().text(query, max_results=settings.max_search_results)
        return [
            {
                "title": search_result.get("title"),
                "url": search_result.get("href"),
                "snippet": search_result.get("body"),
            }
            for search_result in search_results
        ]
    except Exception:
        print(f"Error fetching URL: {query}")
        return []

def read_url(url: str) -> str:
    pass
