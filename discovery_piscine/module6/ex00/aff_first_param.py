#!/usr/bin/env python3
import sys
# print(f"Number of parameters: {len(sys.argv) - 1}.") 

# Check if at least one parameter was passed
if len(sys.argv) > 1:
    print(sys.argv[1])
else:
    print("none")