import re

def process_medical_log(log_line):
    """
    Automated Medical Log Processor:
    1. Standardizes Indian 10-digit phone numbers to +91-XXXXX-XXXXX.
    2. Converts Python-style comments (#) to C-style (//).
    3. Safely extracts Process IDs (PID) for system monitoring.
    """
    
    # Tool 1: Format Indian mobile numbers to International format
    # Example: 9876543210 -> +91-98765-43210
    formatted_log = re.sub(r"\b(\d{5})(\d{5})\b", r"+91-\1-\2", log_line)
    
    # Tool 2: Convert Python-style comments to C-style
    # Example: #Urgent -> //Urgent
    cleaned_log = re.sub(r"#+", r"//", formatted_log)
    
    # Tool 3: Extract PID with a safety check
    # Searches for values inside square brackets, e.g., [12345]
    pid_match = re.search(r"\[(\d+)\]", cleaned_log)
    
    # If no PID is found, return "N/A" instead of crashing
    pid = pid_match[1] if pid_match else "N/A"
    
    return f"Status: Success | Log Output: {cleaned_log} | ProcessID: {pid}"

# --- System Testing ---
log1 = "Patient contact: 9876543210, Status: Stable #Urgent_Review"
log2 = "System diagnostic: Process[98765] running #Routine_Maintenance"

print(process_medical_log(log1))
print(process_medical_log(log2))