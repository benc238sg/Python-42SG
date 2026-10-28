#!/usr/bin/env python3
import sys

# def main():
    # Exclude the script name (sys.argv[0]) to get actual parameters
params = sys.argv[1:]

    # Check if no parameters were provided
if not params:
    print("none")
else:
    print(f"parameters: {len(params)}")
        # Loop through each parameter using a 'for' loop
    for para in params:
        print(f"{para}: {len(para)}")