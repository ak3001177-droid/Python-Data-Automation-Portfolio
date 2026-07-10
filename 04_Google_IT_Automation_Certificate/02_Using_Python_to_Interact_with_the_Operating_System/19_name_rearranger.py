import re

def rearrange_name(name):
    # Pattern: Lastname (group 1), comma-space, Firstname (group 2)
    result = re.search(r"^([\w\.-]*), ([\w\.-]*)$", name)
    
    if result is None:
        return name
        
    # Using backreferences to reorder names
    return "{} {}".format(result[2], result[1])

# Test
print(rearrange_name("Lovelace, Ada"))  # Output: Ada Lovelace