#!/usr/bin/env python3
import sys

def main():
    # Verify that exactly one string parameter is passed to the script
    if len(sys.argv) != 2:
        print("none")
        return   
    input_string = sys.argv[1]
    # Count the exact lowercase 'z' characters present in the string
    z_count = input_string.count('z')

    # Print 'z' repeated by the count, or 'none' if there are no 'z's
    if z_count > 0:
        print('z' * z_count)
    else:
        print("none")

if __name__ == "__main__":
    main()