import re
import csv

# Medical Domain Data: Machine Error Codes
# Machine-A format: ERR-2026-X (Old) -> Machine-B format: FIX-2026-X (New)

def contains_machine_error(report_string):
    """Scans the report to check if it contains the Machine-A error code."""
    pattern = r"ERR-2026-\d+" # Regex pattern to identify the specific error
    if re.search(pattern, report_string):
        return True
    return False

def upgrade_machine_code(report_string):
    """Replaces the old error code with the new upgraded code."""
    # Using capturing group to reuse the specific error number in replacement
    pattern = r"ERR-(2026-\d+)"
    return re.sub(pattern, r"FIX-\1", report_string)

def main():
    # Input file containing all patient reports
    report_file = 'hospital_reports.csv'
    
    # List to store processed data
    updated_reports = []

    with open(report_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            patient_id, report_text = row
            
            if contains_machine_error(report_text):
                print(f"Audit Found: Error in Patient {patient_id}. Upgrading...")
                upgraded_text = upgrade_machine_code(report_text)
                updated_reports.append([patient_id, upgraded_text])
            else:
                updated_reports.append([patient_id, report_text])

    # Saving the 'Audit-Verified' new file
    with open('verified_reports.csv', 'w') as out:
        writer = csv.writer(out)
        writer.writerows(updated_reports)
    
    print("Audit Complete: Verified reports saved!")

if __name__ == "__main__":
    main()