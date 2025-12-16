def add_student():
    name = input("Enter name: ")
    marks = input("Enter marks: ")
    with open("students.txt", "a") as f:
        f.write(name + "," + marks + "\n")

def view_students():
    with open("students.txt", "r") as f:
        for line in f:
            name, marks = line.strip().split(",")
            print("Name:", name, "| Marks:", marks)

while True:
    print("\n1.Add Student\n2.View Students\n3.Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        add_student()
    elif ch == "2":
        view_students()
    elif ch == "3":
        break
password = input("Enter password: ")

strength = 0
if len(password) >= 8:
    strength += 1
if any(c.isupper() for c in password):
    strength += 1
if any(c.isdigit() for c in password):
    strength += 1
if any(c in "!@#$%^&*" for c in password):
    strength += 1

if strength >= 3:
    print("Strong Password")
else:
    print("Weak Password")
