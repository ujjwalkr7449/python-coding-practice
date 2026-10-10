students = []


def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    student = {
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)

    print("Student added successfully!")


def show_students():

    if not students:
        print("No students found")
        return

    for student in students:
        print("----------------")
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])


def search_student():

    name = input("Enter student name: ")

    for student in students:

        if student["name"].lower() == name.lower():
            print("Student found")
            print(student)
            return

    print("Student not found")


def delete_student():

    name = input("Enter student name: ")

    for student in students:

        if student["name"].lower() == name.lower():
            students.remove(student)
            print("Student deleted")
            return

    print("Student not found")


while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
        
        
#Second Largest
numbers = [10, 20, 5, 40, 30]

unique_numbers = list(set(numbers))

unique_numbers.sort()

print("Second largest:", unique_numbers[-2])
#Problem 3 — Remove duplicates
numbers = [1, 2, 2, 3, 4, 4, 5]

result = list(set(numbers))

print(result)


numbers = [1, 2, 2, 3, 3, 3]

frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

print(frequency)