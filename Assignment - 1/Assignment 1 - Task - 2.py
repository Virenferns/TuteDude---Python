"""
Problem Statement: Write a Python program that:
1. Takes a user's first name and last name as input.
2. Concatenates the first name and last name into a full name.
3. Prints a personalized greeting message using the full name.
"""

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

fullname = first_name + " " + last_name

result = "Hello, "+ fullname + "! Welcome to the Python program."

print(result)