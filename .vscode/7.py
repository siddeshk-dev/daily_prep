import os

USERS_FILE = "users.txt"
TRANSACTION_FILE = "transactions.txt"


# ---------------- FILE CHECK ----------------
def initialize_files():
    if not os.path.exists(USERS_FILE):
        open(USERS_FILE, "w").close()
    if not os.path.exists(TRANSACTION_FILE):
        open(TRANSACTION_FILE, "w").close()


# ---------------- ACCOUNT FUNCTIONS ----------------
def create_account():
    print("\n--- Create Account ---")
    username = input("Enter username: ")
    password = input("Enter password: ")
    balance = 0

    with open(USERS_FILE, "a") as f:
        f.write(f"{username},{password},{balance}\n")

    print("✅ Account created successfully!")


def login():
    print("\n--- Login ---")
    username = input("Username: ")
    password = input("Password: ")

    with open(USERS_FILE, "r") as f:
        for line in f:
            u, p, b = line.strip().split(",")
            if u == username and p == password:
                print("✅ Login successful!")
                return username, int(b)

    print("❌ Invalid login!")
    return None, None


def update_balance(username, new_balance):
    lines = []
    with open(USERS_FILE, "r") as f:
        lines = f.readlines()

    with open(USERS_FILE, "w") as f:
        for line in lines:
            u, p, b = line.strip().split(",")
            if u == username:
                f.write(f"{u},{p},{new_balance}\n")
            else:
                f.write(line)


# ---------------- BANK OPERATIONS ----------------
def log_transaction(username, action, amount):
    with open(TRANSACTION_FILE, "a") as f:
        f.write(f"{username},{action},{amount}\n")


def deposit(username, balance):
    amount = int(input("Enter deposit amount: "))
    balance += amount
    update_balance(username, balance)
    log_transaction(username, "Deposit", amount)
    print("💰 Deposit successful!")
    return balance


def withdraw(username, balance):
    amount = int(input("Enter withdraw amount: "))
    if amount > balance:
        print("❌ Insufficient balance!")
    else:
        balance -= amount
        update_balance(username, balance)
        log_transaction(username, "Withdraw", amount)
        print("💸 Withdraw successful!")
    return balance


def check_balance(balance):
    print("💳 Current Balance:", balance)


def view_transactions(username):
    print("\n--- Transaction History ---")
    with open(TRANSACTION_FILE, "r") as f:
        for line in f:
            u, action, amount = line.strip().split(",")
            if u == username:
                print(f"{action}: ₹{amount}")


# ---------------- USER MENU ----------------
def user_menu(username, balance):
    while True:
        print("\n--- Bank Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transactions")
        print("5. Logout")

        choice = input("Choose: ")

        if choice == "1":
            balance = deposit(username, balance)
        elif choice == "2":
            balance = withdraw(username, balance)
        elif choice == "3":
            check_balance(balance)
        elif choice == "4":
            view_transactions(username)
        elif choice == "5":
            print("👋 Logged out!")
            break
        else:
            print("❌ Invalid option!")


# ---------------- MAIN MENU ----------------
def main():
    initialize_files()

    while True:
        print("\n=== BANK SYSTEM ===")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Select: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            user, balance = login()
            if user:
                user_menu(user, balance)
        elif choice == "3":
            print("👋 Thank you!")
            break
        else:
            print("❌ Invalid choice!")


# ---------------- RUN PROGRAM ----------------
main()
