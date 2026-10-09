numbers = [10, 20, 30, 40, 50]

print(numbers)
#indexing
numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[2])
print(numbers[-1])

#3. Find maximum/minimum
numbers = [10, 50, 20, 80, 30]

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

#reverse
numbers = [10, 20, 30, 40, 50]

print(numbers[::-1])

#Sum of list
numbers = [10, 20, 30, 40, 50]

total = 0

for num in numbers:
    total += num

print("Sum:", total)