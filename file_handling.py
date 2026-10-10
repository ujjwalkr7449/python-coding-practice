#1. Write file
with open("user.txt", "w") as file:
    file.write("Name: Ujjwal\n")
    file.write("Age: 22\n")
    file.write("City: Patna\n")
    
#Read file 
with open("user.txt", "r") as file:
    data = file.read()

print(data)