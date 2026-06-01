# pipeline.py
# PURPOSE: Run the full pipeline — retrieval → enrichment → scrubbing → external LLM

from retriever import retrieve_context
from enricher import enrich_query
from scrubber import scrub_pii
from router import get_external_response

def run_pipeline(user_query: str, model: str = "claude-opus-4-5") -> dict:
    """
    Full pipeline for a single employee query.
    Returns a dict with intermediate steps (for transparency/debugging).
    """
    print(f"\n{'='*50}")
    print(f"Query: {user_query}")
    print('='*50)

    # Step 1: Retrieve relevant company context
    context = retrieve_context(user_query)
    print(f"\nRetrieved {len(context)} chars of context.")

    # Step 2: Enrich the query using DeepSeek
    enriched = enrich_query(user_query, context)

    # Step 3: Scrub PII before sending externally
    safe_prompt = scrub_pii(enriched)
    print(f"PII scrubbing applied.")

    # Step 4: Get response from external LLM
    final_response = get_external_response(safe_prompt, model=model)

    return {
        "query": user_query,
        "retrieved_context": context,
        "enriched_prompt": enriched,
        "safe_prompt": safe_prompt,
        "final_response": final_response
    }


# Test end-to-end
if __name__ == "__main__":
    result = run_pipeline("What do my projections look like this month?")
    print("\nFinal Response:\n")
    print(result["final_response"])