"""
Task 2: Write and Append Data to a File

Problem Statement: Write a Python program that:
1. Takes user input and writes it to a file named output.txt.
2. Appends additional data to the same file.
3. Reads and displays the final content of the file.
"""

input_text = input("Enter the contents of your text file: ")

with open("output.txt", "wt") as file_write:
    file_write.write(input_text)

additional_text = input("Enter the additional contents of your text file: ")

with open("output.txt", "at") as file_append:
    file_append.write('\n')
    file_append.write(additional_text)

with open("output.txt", "rt") as file_read:
    data = file_read.read()

    print(f"Final contents of output.txt:")
    print(data)