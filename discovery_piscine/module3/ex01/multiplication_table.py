#!/usr/bin/env python3

print ("Let's look at the multiplication table.")
num1 = int(input("Enter a number\n"))
count = 10
j = 0
while count>0:
	result = j*num1
	print(f"{j} x {num1} = {result}")
	j += 1
	count -= 1

print("Thank you.")
