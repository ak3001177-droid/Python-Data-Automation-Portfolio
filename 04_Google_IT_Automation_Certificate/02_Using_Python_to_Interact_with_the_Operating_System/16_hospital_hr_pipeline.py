import csv

# ==========================================
# PHASE 0: Setup (Creating a dummy CSV file)
# ==========================================
def create_hospital_data(filename):
    # This creates a raw CSV file so you can test the code immediately
    with open(filename, 'w') as f:
        f.write("Name, Role, Ward\n")
        f.write("Amit, Nurse, ICU\n")
        f.write("Priya, Doctor, OPD\n")
        f.write("Rahul, Ward Boy, ICU\n")
        f.write("Neha, Surgeon, Surgery\n")
        f.write("Karan, Nurse, OPD\n")
        f.write("Simran, Doctor, ICU\n")
    print(f"[*] Dummy data created in '{filename}'")


# ==========================================
# PHASE 1: The Data Collector (Reader)
# ==========================================
def read_hospital_staff(csv_file_location):
    # Registering a rulebook to ignore extra spaces after commas
    csv.register_dialect('hospitalDialect', skipinitialspace=True, strict=True)
    
    # Opening the file with our smart VIP scanner
    staff_file = csv.DictReader(open(csv_file_location), dialect='hospitalDialect')
    
    # The empty bag to store all ID cards (Dictionaries)
    staff_list = []
    for data in staff_file:
        # dict(data) ensures the row is strictly converted to a dictionary
        staff_list.append(dict(data)) 
        
    return staff_list


# ==========================================
# PHASE 2: The HR Brain (Data Processor)
# ==========================================
def count_staff_by_ward(staff_list):
    # Empty list to collect just the Ward names
    ward_list = []
    for staff_data in staff_list:
        ward_list.append(staff_data['Ward'])
    
    # Empty dictionary (The Diary) to store the final counts
    ward_counts = {}
    
    # set() removes duplicates so we only count unique wards
    for ward_name in set(ward_list):
        ward_counts[ward_name] = ward_list.count(ward_name)
        
    return ward_counts


# ==========================================
# PHASE 3: The Typist (Report Writer)
# ==========================================
def generate_hr_report(dictionary, report_file):
    # Open a new text file to write the final summary
    with open(report_file, "w+") as f:
        # sorted() ensures the wards are printed in A to Z order
        for k in sorted(dictionary):
            # Combine the Ward name, a colon, the count, and a new line (Enter key)
            f.write(str(k) + ':' + str(dictionary[k]) + '\n')
            
    print(f"[*] Final report successfully generated in '{report_file}'")


# ==========================================
# MAIN EXECUTION (Running the Hospital Pipeline)
# ==========================================
csv_filename = "hospital_staff.csv"
report_filename = "ward_staff_report.txt"

# 1. Generate the raw data
create_hospital_data(csv_filename)

# 2. Read the raw CSV into a Python list of dictionaries
all_staff_data = read_hospital_staff(csv_filename)

# 3. Process the data to get the count of staff per ward
ward_summary = count_staff_by_ward(all_staff_data)

# 4. Write the final calculated data into a neat text report
generate_hr_report(ward_summary, report_filename)