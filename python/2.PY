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

