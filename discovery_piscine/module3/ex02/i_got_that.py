#!/usr/bin/env python3

command = "STOP"
phrase = input("What you gotta say : ")
while phrase != command: 
    phrase = input ("I got that! Anything else? : ")

    if phrase == command:
        break

#if phrase == command
#        print("Thank you.")
#else:
#        i = 0
#	min_len = min(len(command), len(phrase))
#        while i<min_len: 
#                print(f"Inside the loop, my variable is {num1}")
#                num1 = num1+1
#                count -= 1
