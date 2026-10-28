#!/usr/bin/env python3

original_list = [2, 8, 9, 48, 8, 22, -12, 2]

# Initialize an empty set to collect the modified values > 5
output_set = set()

for num in original_list:
    if num > 5:
        output_set.add(num + 2)

# Display the original list and the unique resulting set
print(original_list)
print(output_set)