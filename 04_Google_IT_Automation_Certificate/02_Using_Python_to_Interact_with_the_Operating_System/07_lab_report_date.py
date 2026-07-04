import os
import datetime

def check_lab_report_date(report_filename):
    # Generate a new blank lab report file
    with open(report_filename, "w") as file:
        pass
    
    # Extract the raw modification timestamp (in seconds) from the OS
    raw_timestamp = os.path.getmtime(report_filename)
    
    # Convert the raw timestamp into a readable datetime format
    clean_datetime = datetime.datetime.fromtimestamp(raw_timestamp)
    
    # Slice the string to extract only the first 10 characters (yyyy-mm-dd)
    final_date = str(clean_datetime)[:10]
    
    return final_date

print("Lab Report Generation Date:")
print(check_lab_report_date("blood_test_report.txt"))