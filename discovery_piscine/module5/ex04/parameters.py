#!/usr/bin/env python3
import sys

# sys.argv[0] is always the script name itself, 
# so we subtract 1 to get the count of actual parameters passed.
# num_parameters = len(sys.argv) - 1
# print(f"Number of parameters: {num_parameters}.")
print(f"Number of parameters: {len(sys.argv) - 1}.") 
#This works too