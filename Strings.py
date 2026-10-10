text = "Python"

print(len(text))
print(text.upper())
print(text.lower())
print(text[0])
print(text[-1])

#Palindrome check
text = input("Enter string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")