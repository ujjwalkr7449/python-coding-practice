#1. Divide by zero
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero")
    
#Invalid input
try:
    age = int(input("Enter your age: "))
    print("Age:", age)

except ValueError:
    print("Please enter a valid number")