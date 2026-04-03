"""
Task 2: Sum of Integers from 1 to 50 Using a Loop

Problem Statement: Write a Python program that:
1. Uses a for loop to iterate over numbers from 1 to 50.
2. Calculates the sum of all integers in this range.
3. Displays the final sum.
"""

number_to_sum = 0
for number in range(1, 51):
    number_to_sum += number

print(f" Sum of numbers from 1 to 50 is: {number_to_sum}")


