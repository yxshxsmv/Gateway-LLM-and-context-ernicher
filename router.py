# router.py
# PURPOSE: Send the enriched, scrubbed prompt to an external LLM (Claude, GPT-4o, etc.)

import os
import litellm
from dotenv import load_dotenv

load_dotenv()

# Change this to switch models: "gpt-4o", "grok-beta", etc.
DEFAULT_MODEL = "claude-opus-4-5"

def get_external_response(enriched_prompt: str, model: str = DEFAULT_MODEL) -> str:
    """
    Sends the enriched prompt to an external LLM.
    Returns the response text.
    """
    print(f"Sending to {model}...")
    
    response = litellm.completion(
        model=model,
        messages=[
            {"role": "user", "content": enriched_prompt}
        ]
    )
    
    return response.choices[0].message.content


# Test it
if __name__ == "__main__":
    test_prompt = "Based on Q3 data showing $420K against a $500K target, what recommendations would you make for the remaining weeks?"
    result = get_external_response(test_prompt)
    print("External LLM Response:\n")
    print(result)