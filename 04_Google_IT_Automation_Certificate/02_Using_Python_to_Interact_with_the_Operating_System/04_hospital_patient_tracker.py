print("\n--- STEP 1: Admitting Initial Patients ---")
# Open file in 'write' mode to create it and add initial patients
initial_patients = ["Rahul", "Anjali", "Ramesh", "Sunita", "Vikram"]

with open("patients.txt", "w") as file:
    for patient in initial_patients:
        file.write(patient + "\n")

print("Initial patients admitted successfully.")


print("\n--- STEP 2: Emergency Admissions (Appending) ---")
# Open file in 'append' mode to add new patients without deleting old ones
new_admissions = ["Suresh", "Pooja", "Deepak"]

with open("patients.txt", "a") as file:
    for patient in new_admissions:
        file.write(patient + "\n")

print("New emergency patients added to the record.")


print("\n--- STEP 3: Discharging Patients ---")
# Reading current patients into a list
discharged_patients = ["Anjali", "Ramesh", "Vikram"]
temp_list = []

with open("patients.txt", "r") as file:
    for p in file:
        temp_list.append(p.strip()) #strip() removes any leading/trailing whitespace or newline characters like '\n'

# Opening in 'write' mode to overwrite the file with ONLY remaining patients
with open("patients.txt", "w") as file:
    for name in temp_list:
        if name not in discharged_patients:
            file.write(name + "\n")

print("Discharged patients removed from the active file.")


print("\n--- STEP 4: Final Ward Inspection (Checking Status) ---")
# Reading the final file to check if specific patients are still admitted
patients_to_check = ["Rahul", "Anjali"]
active_patients = []

with open("patients.txt", "r") as file:
    for p in file:
        active_patients.append(p.strip())

for check in patients_to_check:
    if check in active_patients:
        print(f"STATUS: {check} is currently ADMITTED in the ward.")
    else:
        print(f"STATUS: {check} has been DISCHARGED.")

print("\n==========================================\n")