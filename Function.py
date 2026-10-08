def greet():
    print("Hello Ujjwal")


greet()

#2. Function with parameters
def greet(name):
    print("Hello", name)


greet("Ujjwal")

#3. Function with return
def add(a, b):
    return a + b


result = add(10, 20)

print(result)

#factorial
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


num = int(input("Enter number: "))

print("Factorial:", factorial(num))

#Prime no. function
def is_prime(num):

    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


num = int(input("Enter number: "))

if is_prime(num):
    print("Prime")
else:
    print("Not Prime")