def perform_operations(num1, num2):
    # Addition
    addition_result = num1 + num2
    print(f"Addition: {num1} + {num2} = {addition_result}")
 
    # Subtraction
    subtraction_result = num1 - num2
    print(f"Subtraction: {num1} - {num2} = {subtraction_result}")
 
    # Multiplication
    multiplication_result = num1 * num2
    print(f"Multiplication: {num1} * {num2} = {multiplication_result}")
 
    # Division
    # Checking if num2 is zero to avoid division by zero error
    if num2 != 0:
        division_result = num1 / num2
        print(f"Division: {num1} / {num2} = {division_result}")
    else:
        print("Division by zero is undefined.")
 
# User input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
 
# Performing operations
perform_operations(num1, num2)

# math_operations.py

# Function to calculate the square of a number
def square(num):
    return num * num

# Function to calculate the sum of two numbers
def add(a, b):
    return a + b

    # Import the math_operations module
import math_operations

# Call the functions from the module
result1 = math_operations.square(5)
print("Square of 5:", result1)

result2 = math_operations.add(3, 7)
print("Sum of 3 and 7:", result2)
