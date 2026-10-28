#!/usr/bin/env python3
import sys

def main():
    # sys.argv[0] is the script name, so we need exactly 3 elements in total
    if len(sys.argv) != 3:
        print("none")
        return

    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        
        # Construct an inclusive list matching the example [10, 11, 12, 13, 14]
        result = list(range(start, end + 1))
        print(result)
        
    except ValueError:
        print("none")

if __name__ == "__main__":
    main()