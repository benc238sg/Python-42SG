#!/usr/bin/env python3
Num1 = int(input("Enter the first number: "))
Num2 = int(input("Enter the second number: "))
Num_result = Num1*Num2

if Num_result<0: 
	print("The result is negative.")
elif Num_result>0:
	print("The result is positive.")
else: 
 	print("The result is positive and negative.")
