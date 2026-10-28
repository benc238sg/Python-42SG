#!/usr/bin/env python3
num_input = input("Give me a number: ")

# Convert the string input into a float
num = float(num_input)

# Check if the float is a whole number (integer)
if num.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")