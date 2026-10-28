#!/usr/bin/env python3
import sys

def main():
    # Exclude the script name from arguments
    params = sys.argv[1:]

    # If there are no parameters, display 'none'
    if not params:
        print("none")
        return

    # Process each parameter passed as an argument
    for param in params:
        # Use .find() to check if 'ism' is at the very end of the string
        # If 'ism' is at the end, its index will equal len(param) - 3
        pos = param.find('ism', len(param) - 3)
        
        # If 'ism' is not found at the end, pos will be -1
        if pos == -1:
            print(f"{param}ism")

if __name__ == "__main__":
    main()