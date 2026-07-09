import re

def scan_medical_log(log_text):
    print(f"Scanning Log: '{log_text}'")
    
    # Tool 1: OR (|) & Optional (?) -> Dhoondho ki kya Dr. Sharma ya Dr. Singh ka zikr hai?
    # 'Dr' ke baad dot optional (\.?) hai.
    doc_pattern = r"Dr\.? (Sharma|Singh)"
    doc_match = re.search(doc_pattern, log_text)
    if doc_match:
        # Match milne par sirf pattern ka main hissa (group 0) print karo
        print(f"[*] Doctor Found: {doc_match[0]}")

    # Tool 2: Wildcard & Star (.*) -> Bimari (Condition) ka aage ka poora sentence nikal lo
    cond_pattern = r"Condition: .*"
    cond_match = re.search(cond_pattern, log_text)
    if cond_match:
        print(f"[*] Extracted Info: {cond_match[0]}")

    # Tool 3: The NOT Operator ([^...]) -> Check karo kya text mein koi ajeeb symbol (@, #, !) toh nahi hai?
    # Rule: Letters, numbers, space, dot aur colon ke alawa kuch bhi ho toh flag kar do
    weird_symbol_pattern = r"[^a-zA-Z0-9 \.:]"
    weird_match = re.search(weird_symbol_pattern, log_text)
    if weird_match:
        print(f"[!] Warning: Ajeeb symbol '{weird_match[0]}' pakda gaya log mein!")
        
    print("=" * 45)

# Test Cases
scan_medical_log("Dr. Sharma checked PAT-101. Condition: Severe Dengue.")
scan_medical_log("Dr Singh reported an error! Condition: Unknown Virus")