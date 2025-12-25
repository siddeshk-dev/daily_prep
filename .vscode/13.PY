import os

FILE_NAME = "employees.txt"

def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    role = input("Enter Role: ")
    salary = input("Enter Salary: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{emp_id},{name},{role},{salary}\n")

    print(" Employee Added Successfully")

def view_employees():
    if not os.path.exists(FILE_NAME):
        print(" No employee records found")
        return

    print("\n--- Employee List ---")
    with open(FILE_NAME, "r") as file:
        for line in file:
            emp_id, name, role, salary = line.strip().split(",")
            print(f"ID:{emp_id} | Name:{name} | Role:{role} | Salary:{salary}")

def search_employee():
    search_id = input("Enter Employee ID to search: ")

    found = False
    with open(FILE_NAME, "r") as file:
        for line in file:
            emp_id, name, role, salary = line.strip().split(",")
            if emp_id == search_id:
                print("\n Employee Found")
                print(f"Name: {name}")
                print(f"Role: {role}")
                print(f"Salary: {salary}")
                found = True
                break

    if not found:
        print(" Employee not found")

def main_menu():
    while True:
        print("\n====== Employee Management System ======")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            print(" Exiting system...")
            break
        else:
            print(" Invalid choice")

main_menu()
