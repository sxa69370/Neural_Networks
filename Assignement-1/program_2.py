#  Question: Take two numbers from user and perform at least 4 arithmetic operations on them. 

# Take two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform arithmetic operations
sum = num1 + num2
difference = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Divison by zero not possible"

# Print the results
print("Sum: ",sum)
print("Difference: ",difference)
print("Multiplication: ",multiplication)
print("Division: ",division)