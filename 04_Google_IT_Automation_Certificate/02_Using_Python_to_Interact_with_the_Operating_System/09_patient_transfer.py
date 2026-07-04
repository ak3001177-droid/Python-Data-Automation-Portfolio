import os

def transfer_patient_record():
    # Define the current ward and the destination ICU ward paths
    current_ward = os.getcwd()
    icu_ward = os.path.join(current_ward, "ICU_Department")
    
    # Create the ICU ward directory safely if it does not exist
    if not os.path.exists(icu_ward):
        os.mkdir(icu_ward)
        
    # Create a dummy patient record in the current general ward
    src_file = os.path.join(current_ward, "patient_amit.txt")
    with open(src_file, "w") as file:
        file.write("Patient Amit: Needs immediate ICU Transfer.")
        
    # Define the exact destination path for the patient record
    dest_file = os.path.join(icu_ward, "patient_amit.txt")
    
    # Move the file from the general ward to the ICU ward using rename
    os.rename(src_file, dest_file)
    print("Transfer Complete: Patient record successfully moved to ICU.")

transfer_patient_record()