"""
Problem Statement: Write a Python program that does the following:
1. Takes two numbers as input from the user.
2. Performs the basic mathematical operations on these two
numbers:
o Addition
o Subtraction
o Multiplication
o Division
3. Displays the results of each operation on the screen.
"""

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition: ", int(a + b))
print("Subtraction: ", int(a - b))
print("Multiplication: ", int(a * b))
print("Division: ", a / b)