print("hello world")
name='ujjwal'
age=22
city="bhagalpur"

print("Name:",name)
print('Age:',age)
print("City:", city)

print(f"My name is {name}, I am {age} years old and I live in {city}.")
print(type(name))
print(type(age))

#Type Casting 
age=int(age)
print(age)
print(type(age))


name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")


a = 10
b = 20

a, b = b, a

print("a =", a)
print("b =", b)

a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

#1. Area of circle
radius = float(input("Enter radius: "))

area = 3.14159 * radius * radius

print("Area of circle:", area)
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Temperature in Fahrenheit:", fahrenheit)

fahrenheit = float(input("Enter temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5 / 9

print("Temperature in Celsius:", celsius)
#3. Simple Interest
principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest:", simple_interest)