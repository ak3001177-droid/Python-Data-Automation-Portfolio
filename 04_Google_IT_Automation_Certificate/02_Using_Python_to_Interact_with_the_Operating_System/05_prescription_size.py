import os

def create_patient_prescription(patient_filename):
    # Medical notes to be written inside the prescription
    medical_notes = "Patient Name: Rahul\nDiagnosis: Viral Fever\nMedicines: Paracetamol 500mg, Rest for 3 days."
    
    # Create a new file in write mode and add the medical notes
    with open(patient_filename, "w") as file:
        file.write(medical_notes)
    
    # Measure the size of the prescription file in bytes
    file_weight = os.path.getsize(patient_filename)
    return file_weight

print("Prescription File Size (in bytes):")
print(create_patient_prescription("rahul_prescription.txt"))