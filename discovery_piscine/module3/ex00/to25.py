#!/usr/bin/env python3

#print ("Let count to 25.")
num1 = int(input(f"Enter a number less than 25: \n"))
if num1>25:
	print("Error")
else:
	count = 25-num1
	while count>=0: 
		print(f"Inside the loop, my variable is {num1}")
		num1 = num1+1
		count -= 1

print("Thank you.")
