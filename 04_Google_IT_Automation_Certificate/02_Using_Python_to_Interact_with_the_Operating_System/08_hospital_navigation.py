import os

def go_to_main_hospital_building():
    # Create a relative path pointing to the parent directory (one level up)
    relative_path_to_main = os.path.join(os.getcwd(), "..")
    
    # Convert the relative path into a clean, absolute directory path
    clean_main_path = os.path.abspath(relative_path_to_main)
    
    return clean_main_path

print("Absolute Path to the Main Hospital Building (Parent Directory):")
print(go_to_main_hospital_building())