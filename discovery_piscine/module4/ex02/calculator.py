#!/usr/bin/env python3
UserNum1 = input(f"Give me the first number: ")
UserNum2 = input(f"Give me the second number: ")
num1 = int(float(UserNum1))
num2 = int(float(UserNum2))

print("Thank you!")
print(f"{num1} + {num2} = {int(num1 + num2)}")
print(f"{num1} - {num2} = {int(num1 - num2)}")
print(f"{num1} / {num2} = {int(float(num1 / num2))}")
print(f"{num1} * {num2} = {int(num1 * num2)}")

# Format as integers in the output if they are whole numbers to match the example exactly
# n1 = int(num1) if num1.is_integer() else num1
# n2 = int(num2) if num2.is_integer() else num2

# print("Thank you!")
# print(f"{n1} + {n2} = {int(num1 + num2) if (num1 + num2).is_integer() else num1 + num2}")
# print(f"{n1} - {n2} = {int(num1 - num2) if (num1 - num2).is_integer() else num1 - num2}")
# print(f"{n1} / {n2} = {int(num1 / num2) if (num1 / num2).is_integer() else num1 / num2}")
# print(f"{n1} * {n2} = {int(num1 * num2) if (num1 * num2).is_integer() else num1 * num2}")