#!/usr/bin/env python3
import sys

# def main():
    # sys.argv[0] is the script name. 
    # len(sys.argv) must be exactly 2 if 1 parameter is passed.
if len(sys.argv) < 2:
    print("none")
    #    return
keyword = sys.argv[1]
parameter = input("What was the parameter? ")
    # Check if the input matches the parameter
if parameter == keyword:
    print("Good job!")
else:
    print("Nope, sorry...")

# if __name__ == "__main__":
#     main()