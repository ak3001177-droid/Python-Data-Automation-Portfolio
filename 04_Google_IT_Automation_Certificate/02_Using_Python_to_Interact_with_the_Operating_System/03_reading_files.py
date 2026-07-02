# ---------------------------------------------------------
# SCENARIO 1: Without using strip()
# This will print an extra blank line after every sentence
# because text files have a hidden 'newline' character at the end of each line.
# ---------------------------------------------------------

print("\n--- OUTPUT 1: Without strip() ---")

with open("spider.txt") as file:
    for line in file:
        print(line.upper())

# ---------------------------------------------------------
# SCENARIO 2: Using the strip() function
# strip() removes that hidden 'newline' and any extra spaces,
# making the output clean and continuous.
# ---------------------------------------------------------

print("\n--- OUTPUT 2: With strip() ---")

with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())

# ---------------------------------------------------------
# SCENARIO 3: Reading all lines into a list and sorting
# readlines() loads the entire file into system memory as a Python List.
# We must manually close() the file when not using the 'with' block.
# not for large files, as it can consume a lot of memory.
# ---------------------------------------------------------

print("\n--- OUTPUT 3: Sorting a List of Lines ---")

file = open("spider.txt")
lines = file.readlines()
file.close()

lines.sort()
print(lines)

print("\n---------------------------------\n")