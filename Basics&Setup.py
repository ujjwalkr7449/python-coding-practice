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