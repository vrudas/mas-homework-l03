import os

from config import settings


def write_report(filename: str, content: str) -> str:
    path = "./" + settings.output_dir + "/" + filename

    dirpath = os.path.dirname(path) or "."
    os.makedirs(dirpath, exist_ok=True)

    with open(path, 'w', encoding="utf-8") as f:
        f.write(content)

    return f"Report written to {path}"


def web_search(query: str) -> list[dict]:
    pass


def read_url(url: str) -> str:
    pass
