import re

def validate_patient_data(email, patient_id):
    # Rule 1: Email kisi bhi word (\w+) se shuru ho, par strictly '@hospital.com' par khatam ho
    email_pattern = r"^\w+@hospital\.com$"
    email_check = re.search(email_pattern, email)
    
    # Rule 2: ID strictly 'PAT-' se shuru ho, aur uske theek baad sirf numbers (0-9) aane chahiye
    id_pattern = r"^PAT-[0-9]+$"
    id_check = re.search(id_pattern, patient_id)
    
    # bool() function match milne par True aur na milne par False return karta hai
    print(f"Email '{email}' Valid? : {bool(email_check)}")
    print(f"ID '{patient_id}' Valid? : {bool(id_check)}")
    print("-" * 35)

# Test Cases (Checking Good and Bad data)
print("Testing Valid Data:")
validate_patient_data("amit_123@hospital.com", "PAT-1045") 

print("Testing Invalid Data:")
validate_patient_data("amit@gmail.com", "PAT-A123")