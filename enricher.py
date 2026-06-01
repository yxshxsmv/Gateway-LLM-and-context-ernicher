# enricher.py
# PURPOSE: Use DeepSeek R1 (running locally) to combine the user query
#          + retrieved context into a clean, self-contained prompt

import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "deepseek-r1:8b"

SYSTEM_PROMPT = """You are an internal assistant for a company.
You receive an employee's question and relevant internal company documents.
Your job is to write a clear, complete prompt that:
1. Summarizes the relevant context (without leaking sensitive data)
2. States the employee's question precisely
3. Can be sent to an external AI model to get a helpful answer

Be concise. Do not answer the question yourself — just build the prompt."""

def enrich_query(user_query: str, retrieved_context: str) -> str:
    """
    Sends the query + context to DeepSeek running locally via Ollama.
    Returns an enriched prompt ready for the external LLM.
    """
    full_input = f"""
Employee Question: {user_query}

Relevant Internal Context:
{retrieved_context}

Write a self-contained prompt for an external AI model based on the above.
"""
    
    payload = {
        "model": MODEL_NAME,
        "prompt": full_input,
        "system": SYSTEM_PROMPT,
        "stream": False  # Wait for full response
    }
    
    print("Enriching query with DeepSeek R1...")
    response = requests.post(OLLAMA_URL, json=payload)
    result = response.json()
    
    return result["response"]


# Test it directly
if __name__ == "__main__":
    sample_query = "What are my team's projections for this month?"
    sample_context = "Q3 projections for Team Alpha: Revenue target $500K, current tracking at $420K as of Aug 15."
    
    enriched = enrich_query(sample_query, sample_context)
    print("Enriched Prompt:\n")
    print(enriched)