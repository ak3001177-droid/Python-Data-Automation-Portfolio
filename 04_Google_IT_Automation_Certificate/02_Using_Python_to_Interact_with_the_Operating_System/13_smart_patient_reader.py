import csv

def analyze_patient_data(filename):
    # Open the patient records file in read mode
    with open(filename, "r") as report:
        
        # Create a VIP reader that treats the first row as Dictionary Keys (Headings)
        reader = csv.DictReader(report)
        
        # Call the exact column name to print specific data
        for row in reader:
            print("Patient {} is suffering from {}.".format(row["Patient_Name"], row["Disease"]))

# Note: The CSV file must have headings in the first row like:
# Patient_Name, Age, Disease