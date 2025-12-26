import os
import datetime

USERS_FILE = "users.txt"
TRANS_FILE = "transactions.txt"


# ---------- Utility Functions ----------
def log_transaction(username, message):
    with open(TRANS_FILE, "a") as f:
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{time},{username},{message}\n")


def load_users():
    users = {}
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            for line in f:
                username, pin, balance = line.strip().split(",")
                users[username] = {"pin": pin, "balance": int(balance)}
    return users


def save_users(users):
    with open(USERS_FILE, "w") as f:
        for u in users:
            f.write(f"{u},{users[u]['pin']},{users[u]['balance']}\n")


# ---------- Core Functions ----------
def register_user(users):
    username = input("Enter new username: ")

    if username in users:
        print("User already exists.")
        return

    pin = input("Set 4-digit PIN: ")
    if not (pin.isdigit() and len(pin) == 4):
        print("Invalid PIN format.")
        return

    users[username] = {"pin": pin, "balance": 0}
    save_users(users)
    print("User registered successfully.")


def login(users):
    username = input("Username: ")
    pin = input("PIN: ")

    if username in users and users[username]["pin"] == pin:
        print("Login successful.")
        return username
    else:
        print("Invalid credentials.")
        return None


def deposit(users, username):
    amt = input("Enter amount to deposit: ")

    if amt.isdigit():
        amt = int(amt)
        users[username]["balance"] += amt
        save_users(users)
        log_transaction(username, f"Deposited {amt}")
        print("Amount deposited successfully.")
    else:
        print("Invalid amount.")


def withdraw(users, username):
    amt = input("Enter amount to withdraw: ")

    if not amt.isdigit():
        print("Invalid amount.")
        return

    amt = int(amt)
    if amt > users[username]["balance"]:
        print("Insufficient balance.")
    else:
        users[username]["balance"] -= amt
        save_users(users)
        log_transaction(username, f"Withdrawn {amt}")
        print("Amount withdrawn successfully.")


def transfer(users, username):
    target = input("Enter receiver username: ")
    amt = input("Enter amount: ")

    if target not in users:
        print("Receiver not found.")
        return

    if not amt.isdigit():
        print("Invalid amount.")
        return

    amt = int(amt)
    if amt > users[username]["balance"]:
        print("Insufficient balance.")
        return

    users[username]["balance"] -= amt
    users[target]["balance"] += amt
    save_users(users)
    log_transaction(username, f"Transferred {amt} to {target}")
    log_transaction(target, f"Received {amt} from {username}")
    print("Transfer completed successfully.")


def show_transactions(username):
    if not os.path.exists(TRANS_FILE):
        print("No transactions found.")
        return

    print("\nTransaction History:")
    with open(TRANS_FILE, "r") as f:
        for line in f:
            time, user, msg = line.strip().split(",", 2)
            if user == username:
                print(f"{time} - {msg}")


# ---------- Main Program ----------
def main():
    users = load_users()

    while True:
        print("\n==== BANK MANAGEMENT SYSTEM ====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            register_user(users)

        elif choice == "2":
            user = login(users)
            if user:
                while True:
                    print("\n---- USER MENU ----")
                    print("1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Transfer")
                    print("5. Transaction History")
                    print("6. Logout")

                    ch = input("Choose option: ")

                    if ch == "1":
                        print("Current Balance:", users[user]["balance"])
                    elif ch == "2":
                        deposit(users, user)
                    elif ch == "3":
                        withdraw(users, user)
                    elif ch == "4":
                        transfer(users, user)
                    elif ch == "5":
                        show_transactions(user)
                    elif ch == "6":
                        print("Logged out successfully.")
                        break
                    else:
                        print("Invalid option.")

        elif choice == "3":
            print("Application closed.")
            break
        else:
            print("Invalid option.")


main()
