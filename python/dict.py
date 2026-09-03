#Activity 1
def intro(name):
    print("Hello", name)
    print("Welcome to Python!")
name = input("Enter your name: ")
intro(name)

#Activity 2
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
number = int(input("Enter a number: "))
result = factorial(number)
print("Factorial =", result)

#Activity 3
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))
print("Addition =", add(num1, num2))
print("Subtraction =", subtract(num1, num2))
print("multiplication =", multiply(num1, num2))
print("Division =", divide(num1, num2))