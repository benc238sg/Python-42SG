#!/usr/bin/env python3
numbers = [2, 8, 9, 48, 8, 22, -12, 2]

# Create the new list by filtering for values greater than 5 and adding 2
numbersplustwo = []
for num in numbers:
    if num > 5:
        numbersplustwo.append(num + 2)

# Display both lists cleanly to match the expected terminal output
print(numbers)
print(numbersplustwo)