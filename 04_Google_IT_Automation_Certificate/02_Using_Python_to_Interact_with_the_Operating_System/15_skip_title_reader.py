import csv

def read_inventory_safely(filename):
    # Using a blank string (empty paper) to collect all sentences
    inventory_summary = ""

    with open(filename, "r") as file:
        # Create the standard reader
        rows = csv.reader(file)
        
        # MAGIC COMMAND: Skip the first row (the cover page/headings)
        next(rows)
        
        # Process the remaining rows containing the actual data
        for row in rows:
            medicine, quantity, status = row
            inventory_summary += "We have {} units of {} (Status: {})\n".format(quantity, medicine, status)
            
    return inventory_summary

# Note: The CSV file must look something like this:
# medicine,quantity,status
# Paracetamol,500,In Stock
# Syringes,50,Low Stock