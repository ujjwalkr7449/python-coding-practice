#1. Write file
with open("user.txt", "w") as file:
    file.write("Name: Ujjwal\n")
    file.write("Age: 22\n")
    file.write("City: Patna\n")
    
#Read file 
with open("user.txt", "r") as file:
    data = file.read()

print(data)

#3. Append to file
with open("user.txt", "a") as file:
    file.write("Country: India\n")

#4 Count words
with open("user.txt", "r") as file:
    data = file.read()

words = data.split()

print("Number of words:", len(words))
    