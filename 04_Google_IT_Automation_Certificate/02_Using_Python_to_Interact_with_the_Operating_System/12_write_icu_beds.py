import csv

# A List of Lists containing the bed number and patient name
icu_patients = [
    ["Bed-01", "Ramesh Kumar"],
    ["Bed-02", "Sunita Sharma"],
    ["Bed-03", "Amit Singh"]
]

# Open a new CSV file in write mode
with open('icu_bed_status.csv', 'w') as bed_file:
    # Create the basic CSV printer
    writer = csv.writer(bed_file)
    
    # Write the entire bulk data into the file at once
    writer.writerows(icu_patients)

print("ICU bed status successfully written to icu_bed_status.csv")