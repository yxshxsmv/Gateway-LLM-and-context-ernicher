# # scrubber.py
# # PURPOSE: Strip emails, phone numbers, and names before sending to external APIs

# import re

# def scrub_pii(text: str) -> str:
#     """
#     Basic regex-based PII removal.
#     Removes emails, phone numbers, and common ID patterns.
#     """
#     # Remove email addresses
#     text = re.sub(r'\b[\w.-]+@[\w.-]+\.\w{2,}\b', '[EMAIL]', text)
    
#     # Remove phone numbers (various formats)
#     text = re.sub(r'\b(\+?\d[\d\s\-().]{7,}\d)\b', '[PHONE]', text)
    
#     # Remove anything that looks like an employee/account ID (e.g., EMP-12345)
#     text = re.sub(r'\b(EMP|ID|ACC|USR)[-_]?\d{3,}\b', '[ID]', text, flags=re.IGNORECASE)
    
#     return text


# # Test it
# if __name__ == "__main__":
#     sample = "Contact John at john.doe@company.com or call +91-9876543210 (EMP-4521)"
#     print("Before:", sample)
#     print("After: ", scrub_pii(sample))