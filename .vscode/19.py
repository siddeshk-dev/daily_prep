import os
from datetime import datetime

FILE_NAME = "expenses.txt"

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food/Travel/etc): ")
    note = input("Enter note: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILE_NAME, "a") as file:
        file.write(f"{date},{amount},{category},{note}\n")

    print("Expense added successfully.")

def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    total = 0
    print("\nDate | Amount | Category | Note")
    print("-" * 50)

    with open(FILE_NAME, "r") as file:
        for line in file:
            date, amount, category, note = line.strip().split(",")
            print(f"{date} | {amount} | {category} | {note}")
            total += float(amount)

    print("-" * 50)
    print("Total Expense:", total)

def clear_expenses():
    if os.path.exists(FILE_NAME):
        open(FILE_NAME, "w").close()
        print("All expenses cleared.")
    else:
        print("No file to clear.")

def menu():
    while True:
        print("\n--- Smart Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Clear Expenses")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            clear_expenses()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

menu()
