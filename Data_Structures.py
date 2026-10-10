#Data Structures
stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

stack.pop()

print(stack)

#Queue
from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

print(queue)

queue.popleft()

print(queue)

#Frequency counter
numbers = [1, 2, 2, 3, 3, 3, 4]

frequency = {}

for num in numbers:

    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(frequency)


#Simple phone book
phone_book = {}

phone_book["Ujjwal"] = "9876543210"
phone_book["Rahul"] = "9876500000"

name = input("Enter name: ")

if name in phone_book:
    print("Phone:", phone_book[name])
else:
    print("Contact not found")