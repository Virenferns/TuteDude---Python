"""
Task 1: Read a File and Handle Errors

Problem Statement: Write a Python program that:
1. Opens and reads a text file named sample.txt.
2. Prints its content line by line.
3. Handles errors gracefully if the file does not exist.
"""

try:
    with open("sample.txt", "rt") as file:
        print('Reading file contents...')
        data = file.readlines()
except FileNotFoundError as file_err:
    print(f"The file 'sample.txt' was not found")
else:
    for i, line in enumerate(data):
        print(f"Line {i+1}: {line}")