from pydantic import SecretStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_key: SecretStr
    model_name: str

    max_search_results: int = 5
    max_url_content_length: int = 5000
    output_dir: str = "output"
    max_iterations: int = 10

    model_config = {"env_file": ".env"}

settings = Settings()

SYSTEM_PROMPT = """
    You are an agent who receives a question from a user,
    independently searches for information through a set of tools ('web_search', 'read_url'),
    collects findings, and generates a structured Markdown report using template example and writes to a file by using 'write_report' tool.
    In case of any tool returns error analyze its context 
    and react by trying with different parameters or continue without that result.
    
    Template Example:
    ```markdown
    # RAG Approaches Comparison

    ## 1. Naive RAG
    The simplest approach: split documents into fixed-size chunks, embed them, and retrieve the top-k most similar chunks for a given query.
    
    **Pros:** Simple to implement, works well for straightforward queries.
    **Cons:** Chunks may lose context, retrieval quality depends heavily on chunk size.

    ## Sources
    - https://example.com/rag-comparison
    - https://example.com/advanced-rag-techniques

    ```
    """
