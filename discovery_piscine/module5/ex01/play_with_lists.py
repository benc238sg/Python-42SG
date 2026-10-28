#!/usr/bin/env python3
# User enters numbers separated by spaces (e.g., 5 10 15 20)
#user_input = input(f"Enter a list of integers separated by spaces: ")
# Convert the string into a list of integers
#numbers = list(map(int, user_input.split()))
numbers = [2, 8, 9, 48, 8, 22, -12, 2]

# Add 2 to each item
numbers_plus_two = [x + 2 for x in numbers]

print("Original list:", numbers)
#print("Data type:", type(numbers))
print("New list:", numbers_plus_two)

# Iterate and create the new list by adding 2 to each value
# new_list = []
# for num in original_list:
#     new_list.append(num + 2)

# # Display both lists exactly as formatted
# print(f"Original list: {original_list}")
# print(f"New list: {new_list}")