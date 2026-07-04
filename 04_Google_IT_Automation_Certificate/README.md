# Google IT Automation with Python Professional Certificate

This repository contains my practice files, notes, and projects for the Google IT Automation with Python certificate. 

## 🗺️ Certificate Course Structure
This professional certificate consists of 6 courses:
1. Crash Course on Python
2. Using Python to Interact with the Operating System
3. Introduction to Git and GitHub
4. Troubleshooting and Debugging Techniques
5. Configuration Management and the Cloud
6. Automating Real-World Tasks with Python

---

# Course 1: Crash Course on Python (Master Notes)

This section contains my master logic and cheat sheets for the core Python concepts learned in Course 1.

## 📊 Iterable Types Comparison (Data Structures)

| Data Structure | Definition | Mutable? | Iterable? | Example Representation |
| :--- | :--- | :--- | :--- | :--- |
| **List** | Sequential collection of any data type. | Yes (Can add/remove elements) | Yes (By numeric index) | `['a', 'b', 3, 4]` |
| **Tuple** | Sequential collection of any data type. | **No** (Immutable)* | Yes (By numeric index) | `('commander', 'lambda')` |
| **Dictionary** | Stores `key:value` pairs. | Yes (Values and Keys can update) | Yes (Iterates over keys) | `{'a': [42], 'b': [23]}` |
| **Set** | Unordered collection of *unique* elements. | Yes | Yes (No index) | `{'^2', 'mc', 'E'}` |
| **String** | Sequential collection of textual data. | **No** (Immutable) | Yes (Character sequence)| `"call me ishmael"` |

*\*Note: While tuples themselves are immutable, if a tuple contains a mutable object (like a list), that specific list inside the tuple can be modified.*

---

## 🛠️ Essential Dictionary Methods

Dictionaries are faster than lists because they use index keys instead of searching sequentially.

* `dictionary.items()`: Returns a live view of the keys and values (Used for `for key, value in...`).
* `dictionary.keys()`: Returns only the keys.
* `dictionary.values()`: Returns only the values.
* `dictionary.get(key, default)`: Returns the value for a key, or a default value if the key doesn't exist (prevents errors).
* `dictionary.update(other_dictionary)`: Replaces existing entries and adds new ones from another dictionary.
* `dictionary.copy()`: Makes a safe photocopy of the dictionary so the original remains unchanged.
* `del dictionary[key]`: Removes a value using its key.
* `dictionary.clear()`: Deletes all items from the dictionary.

---

## ⚡ The Magic of List Comprehensions

List comprehensions are a powerful and Pythonic way to create new lists from existing sequences in just **one single line** of code. It replaces 3-4 lines of a traditional `for` loop.

### The 3 Golden Rules & Syntax:

**1. Basic Loop (No Conditions)**
* **Rule:** Do something to every item in the sequence.
* **Formula:** `[action  for  item in list]`
* **Example:** Add 2 to every number in a range.
    ```python
    new_list = [n + 2 for n in range(2, 4)] 
    # Output: [4, 5]
    ```

**2. Filtering with 'If' (Condition at the END)**
* **Rule:** If you only want to extract or keep specific items (and ignore the rest), the `if` statement goes at the *end*.
* **Formula:** `[action  for  item in list  if condition]`
* **Example:** Keep only the odd numbers.
    ```python
    odd_nums = [x for x in range(1, 11) if x % 2 != 0]
    ```

**3. Replacing with 'If-Else' (Condition at the BEGINNING)**
* **Rule:** If you want to modify an item based on a condition (Plan A vs Plan B), the entire `if-else` block must go *before* the `for` loop.
* **Formula:** `[action_if_true  if condition  else action_if_false  for  item in list]`
* **Example:** Rename `.hpp` files to `.h`, but leave other files exactly as they are.
    ```python
    old_files = ["program.c", "stdio.hpp", "a.out"]
    
    updated_files = [file.replace(".hpp", ".h") if file.endswith(".hpp") else file for file in old_files]
    # Output: ['program.c', 'stdio.h', 'a.out']
    ```
    ## 🔤 Essential String Methods

Strings are immutable, meaning they cannot be modified directly. These methods return a *new* string.

* `string.upper()` / `string.lower()`: Converts the string to all uppercase or lowercase.
* `string.strip()`: Removes leading and trailing whitespaces (or specific characters).
* `string.count(substring)`: Returns the number of times a substring appears.
* `string.isnumeric()` / `string.isalpha()`: Returns True if the string contains only numbers or only letters.
* `string.replace(old, new)`: Replaces all occurrences of the old substring with the new one.
* `string.split(delimiter)`: Splits a string into a list of strings based on the delimiter (default is space).
* `delimiter.join(list)`: Joins a list of strings into a single string, separated by the delimiter.

---

## 🏗️ Object-Oriented Programming (OOP) Basics

OOP is a way of organizing code by grouping data and the functions that operate on them into "Objects".

* **Class:** The blueprint or template for creating objects. Defined using the `class` keyword.
* **Instance (Object):** A specific, unique occurrence of a class.
* **Attributes:** Variables that belong to an object (its characteristics, like color or weight).
* **Methods:** Functions that belong to a class (its actions or behaviors). 
* **Docstrings:** Brief text inside `""" """` explaining what a class or method does.

### OOP Syntax Example:
```python
class Apple:
    """This class represents an Apple."""
    
    # Constructor method to initialize attributes
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    # A method to describe the apple
    def description(self):
        return "This apple is {} and its flavor is {}.".format(self.color, self.flavor)

# Creating an instance (object) of the Apple class
jonagold = Apple("red", "sweet")

# Calling the method
print(jonagold.description())
# Output: This apple is red and its flavor is sweet.
```
---


# 🚀 COURSE 2: Using Python to Interact with the Operating System

## 📖 Module 1: Getting Your Python On 
This module focuses on the fundamentals of using Python to interact directly with the local Operating System, managing packages, and understanding how to write scripts that monitor system health.

### 🛠️ Key Modules & Concepts Learned

#### 1. Built-in Modules (Standard Library)
No installation required for these modules; they come pre-packaged with Python.
* **`math`**: Used for advanced mathematical operations (e.g., `math.sqrt()`, `math.pi`).
* **`shutil`**: Used for high-level file operations and system checks. 
  * *Example:* `shutil.disk_usage("/")` to monitor free disk space.

#### 2. External Modules (Third-Party)
Require installation using the Python Package Manager (`pip`).
* **`arrow`**: A smarter, more human-friendly library for creating, manipulating, and formatting dates and times.
* **`Pillow` (Imported as `PIL`)**: The modern Python Imaging Library used for generating and manipulating image files via code.
* **`psutil`**: A powerful tool for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors).

### 💻 Scripts Created in this Module
1. **`01_os_basics.py`**: Explored date/time manipulation (Arrow), mathematical calculations (Math), and basic image generation (Pillow).
2. **`02_system_health_check.py`**: Built a real-time system dashboard to monitor Disk Space, CPU Usage, and Battery Status using OS-level commands.

---

## 📖 Module 2: Reading and Writing Files
This module focuses on file operations, memory management while handling large files, encoding standards, and navigating OS directories using Python.

### 🛠️ Key Concepts & Best Practices Learned

#### 1. File Handling Modes
* **`"r"` (Read):** Default mode. Opens file for reading only.
* **`"w"` (Write):** Overwrites the file completely or creates a new one.
* **`"a"` (Append):** Adds new data to the very end of an existing file without deleting old data.
* **`"x"` (Exclusive):** Creates a new file but fails/crashes if the file already exists (Safe Write).
* **`"+"` (Update):** Added to other modes (e.g., `"r+"`, `"w+"`) to allow both reading and writing simultaneously.

#### 2. Memory Management (The Lazy Loading Approach)
* **`readlines()`:** Loads the entire file into memory (RAM) as a list. Good for small files, but crashes the system for massive logs (e.g., 55GB).
* **Iterating via `for line in file:`:** Reads one line at a time, flushes it, and moves to the next. This is the safest way to process massive files without crashing the laptop.

#### 3. Text Formatting & Encoding
* **`strip()`:** A string method used to remove hidden characters (like `\n` newlines) and extra whitespaces from the beginning and end of a line read from a file.
* **`encoding="utf-8"`:** The global standard dictionary for characters. Using `open("file.txt", "w", encoding="utf-8")` ensures that special symbols, emojis, and multiple languages don't turn into corrupted "garbage" text across different operating systems (Windows vs Mac/Linux).

#### 4. Managing Directories & Paths
* **Windows Paths:** Python interprets `\` as escape characters. To safely write paths, use forward slashes (`C:/folder/file.txt`) or double backslashes (`C:\\folder\\file.txt`).
* **`os.getcwd()`:** Retrieves the Current Working Directory (the folder where the terminal is currently operating).

### 💻 Scripts Created in this Module
3. **`03_reading_files.py`**: Demonstrated the difference between reading files normally (which leaves hidden `\n` characters) vs. using `.strip()`, and explored the memory-heavy `.readlines()` method.
4. **`04_hospital_patient_tracker.py`**: A practical, real-world application of File I/O. Used `"w"`, `"a"`, and `"r"` modes to create a dynamic register that can Admit (append), Discharge (filter and rewrite), and Search for patient statuses dynamically.

### 📦 Important Terminal Commands
```bash
# To navigate to a specific folder in the terminal
cd Folder_Name/Sub_Folder

### 🛠️ Advanced OS & File Management (Module 2 - Part 2)

#### 1. Managing Directories (Folders) with `os` Module
* **`os.getcwd()`**: Returns the Current Working Directory (finds exactly where your terminal/script is running).
* **`os.chdir(path)`**: Changes the current directory (like double-clicking to enter a folder).
* **`os.mkdir(path)`**: Creates a brand new, empty directory.
* **`os.rmdir(path)`**: Deletes an empty directory (fails if the folder has files inside).
* **`os.listdir(path)`**: Acts as a scanner; returns a Python list of all files and sub-folders inside a specific directory.

#### 2. Managing Files & Paths with `os.path`
* **`os.remove(path)`**: Permanently deletes a file.
* **`os.rename(source, destination)`**: Renames a file, OR moves a file entirely from one folder to another if the full path is changed.
* **`os.path.exists(path)`**: A radar that returns `True` if a file or folder exists, and `False` if it doesn't (used for safe coding).
* **`os.path.isdir(path)`**: Checks if the given path is a folder (directory) and not just a file.
* **`os.path.getsize(path)`**: Returns the exact size of a file in bytes.
* **`os.path.getmtime(path)`**: Returns the last modification time of a file as a raw Unix timestamp (in seconds since 1970).
* **`os.path.join(dir, file)`**: The safest way to combine folder and file names into a complete path. It automatically uses the correct slash (`\` for Windows, `/` for Mac/Linux).
* **`os.path.abspath(path)`**: Converts a messy relative path (like `..` which means "one folder back") into a clean, absolute system path.

#### 3. Date/Time & String Manipulation
* **`datetime.datetime.fromtimestamp(timestamp)`**: Acts as a translator. Converts a raw OS timestamp (e.g., `1783069460.5`) into a human-readable date and time.
* **String Slicing `[:10]`**: Used to extract specific portions of text. For example, slicing a datetime string to get only the first 10 characters representing the date (`yyyy-mm-dd`).

#### 4. The Modern Approach: `pathlib`
The object-oriented, modern way to handle file paths in Python without repeatedly calling OS functions.
* **`from pathlib import Path`**: Imports the smart Path object.
* **The `/` Operator**: Used to easily join directories and files (e.g., `dest_dir / "README.md"`).
* **Direct Methods**: Allows files/folders to act on themselves (e.g., `path.exists()`, `path.mkdir()`, `path.rename()`).

### 💻 Scripts Created (Medical Automation Theme)
5. **`05_prescription_size.py`**: Created a text file and measured its size using `os.path.getsize()`.
6. **`06_ward_admission.py`**: Automated directory creation and file generation using `os.mkdir`, `os.chdir`, and checked contents with `os.listdir`.
7. **`07_lab_report_date.py`**: Extracted a file's timestamp using `getmtime`, converted it via `datetime`, and used string slicing to format it to `yyyy-mm-dd`.
8. **`08_hospital_navigation.py`**: Handled relative paths (`..`) and converted them to absolute paths using `os.path.abspath()`.
9. **`09_patient_transfer.py`**: Successfully moved a file between directories using `os.rename()`.
10. **`10_modern_transfer_pathlib.py`**: Replicated the file transfer logic using Python's modern `pathlib` module.