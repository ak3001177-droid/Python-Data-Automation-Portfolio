import os

def admit_patient_to_ward(ward_name, patient_record):
    # Check if the Ward directory already exists. If not, create it.
    if os.path.isdir(ward_name) == False:
        os.mkdir(ward_name)

    # Navigate into the specific Ward directory
    os.chdir(ward_name)
    
    # Create a blank medical record file for the new patient
    with open(patient_record, "w") as file:
        pass
    
    # Return the list of all patient records present in this current ward
    patients_in_ward = os.path.listdir(".")
    return patients_in_ward

print("Active Patients in the Ward:")
print(admit_patient_to_ward("ICU_Ward_A", "patient_sunita.txt"))