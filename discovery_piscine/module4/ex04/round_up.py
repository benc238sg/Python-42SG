#!/usr/bin/env python3
num_input = input("Give me a number: ")
num = float(num_input)

# Extract the integer part
integer_part = int(num)

# If there is a decimal remainder, round up by adding 1
if num > integer_part:
    result = integer_part + 1
else:
    result = integer_part

print(result)