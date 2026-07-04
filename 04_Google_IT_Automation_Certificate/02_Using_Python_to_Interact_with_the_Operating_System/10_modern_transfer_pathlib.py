from pathlib import Path

def modern_hospital_transfer():
    # Define the destination ward using the modern Path object
    icu_ward = Path("./Modern_ICU/")
    
    # Create the directory safely using Path methods
    if not icu_ward.exists():
        icu_ward.mkdir()
        
    # Define the source file and create a dummy record
    src_file = Path("./patient_vikas.txt")
    with open(src_file, "w") as file:
        file.write("Patient Vikas: Critical Condition.")
        
    # Construct the destination path using the division (/) operator
    dest_file = icu_ward / "patient_vikas.txt"
    
    # Move the file directly using the smart Path object
    src_file.rename(dest_file)
    print("Modern Transfer Complete: Record moved using Pathlib.")

modern_hospital_transfer()