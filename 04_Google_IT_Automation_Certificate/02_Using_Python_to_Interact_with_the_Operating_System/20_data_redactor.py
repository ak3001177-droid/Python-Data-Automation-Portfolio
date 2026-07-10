import re

def redact_email(text):
    # Pattern: Email regex structure
    email_pattern = r"[\w.%+-]+@[\w.-]+"
    
    # Substituting emails with redacted tag
    redacted_text = re.sub(email_pattern, "[REDACTED]", text)
    return redacted_text

# Test
sample_text = "Contact me at go_nuts95@my.example.com for further info."
print(redact_email(sample_text)) 
# Output: Contact me at [REDACTED] for further info.