#!/usr/bin/env python3
import sys
# print(f"Number of parameters: {len(sys.argv) - 1}.") 

# Check if at least one parameter was passed
if len(sys.argv) < 3:
    print("none")
else:
    i = len(sys.argv) - 1
    while i >= 1:
        print(sys.argv[i])
        i -= 1
# # sys.argv[0] is the script name. 
# # We need fewer than 2 actual arguments (meaning len(sys.argv) < 3) to print 'none'.
# if len(sys.argv) < 3:
#     print("none")
# else:
#     # Slice out the arguments (excluding the script name) and reverse them
#     for param in reversed(sys.argv[1:]):
#         print(param)