import csv

# Data provided as a list of dictionaries
doctors = [
    {"name": "Dr. Verma", "shift": "Night", "ward": "Cardiology"},
    {"name": "Dr. Iyer", "shift": "Morning", "ward": "Neurology"},
    {"name": "Dr. Khan", "shift": "Evening", "ward": "Emergency"}
]

# Define the exact column headers required in the CSV
keys = ["name", "shift", "ward"]

# Open a new file in write mode
with open('doctor_roster.csv', 'w') as roster_file:
    # Create the VIP printer and tell it what the column names are
    writer = csv.DictWriter(roster_file, fieldnames=keys)
    
    # CRITICAL: Print the column headers at the very top of the file
    writer.writeheader()
    
    # Paste all the dictionary data under the correct columns
    writer.writerows(doctors)

print("Doctor roster created with proper column headers.")