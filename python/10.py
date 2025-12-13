def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b

def menu():
    print("=====================================")
    print("         PYTHON CALCULATOR")
    print("=====================================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulus")
    print("7. Exit")
    print("=====================================")

while True:
    menu()

    choice = input("Enter your choice: ")

    if choice == "7":
        print("Exiting calculator...")
        break

    if choice in ["1", "2", "3", "4", "5", "6"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Result =", add(a, b))
        elif choice == "2":
            print("Result =", subtract(a, b))
        elif choice == "3":
            print("Result =", multiply(a, b))
        elif choice == "4":
            print("Result =", divide(a, b))
        elif choice == "5":
            print("Result =", power(a, b))
        elif choice == "6":
            print("Result =", modulus(a, b))
    else:
        print("Invalid choice! Please try again.")
students = []

def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    marks = input("Enter student marks: ")

    student = {
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No students available.\n")
        return

    print("========== STUDENT LIST ==========")
    for i, s in enumerate(students):
        print(f"{i + 1}. Name: {s['name']} | Age: {s['age']} | Marks: {s['marks']}")
    print("==================================\n")

def remove_student():
    view_students()

    choice = int(input("Enter student number to remove: "))
    if 1 <= choice <= len(students):
        students.pop(choice - 1)
        print("Student removed!\n")
    else:
        print("Invalid choice!\n")

def menu():
    print("===================================")
    print("        STUDENT MANAGEMENT")
    print("===================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Remove Student")
    print("4. Exit")
    print("===================================")

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        remove_student()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid option! Try again.\n")
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for ch in text:
    if ch in vowels:
        count += 1
print("Number of vowels:", count)
word = "APPLE"

for i in range(len(word)):
    print(word[i], "is at index", i)

