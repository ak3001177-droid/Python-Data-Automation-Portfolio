import csv

def read_staff_list(filename):
    # Open the file in default read mode
    f = open(filename)
    
    # Create a basic CSV reader machine
    csv_f = csv.reader(f)
    
    # Process each row and unpack the values into 3 variables
    for row in csv_f:
        name, phone, role = row
        print("Staff Name: {}, Contact: {}, Duty Role: {}".format(name, phone, role))
        
    # Always close the file when not using the 'with open' method
    f.close()

# Note: You need a dummy 'staff.csv' file with data to run this properly.
# Example data in staff.csv: 
# Rahul, 9876543210, Nurse