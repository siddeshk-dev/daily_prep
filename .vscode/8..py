import sqlite3
from datetime import datetime

# ---------- DATABASE CONNECTION ----------
conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

# ---------- CREATE TABLES ----------
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    balance INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    action TEXT,
    amount INTEGER,
    date TEXT
)
""")
conn.commit()


# ---------- ACCOUNT FUNCTIONS ----------
def create_account():
    print("\n--- Create Account ---")
    username = input("Username: ")
    password = input("Password: ")

    try:
        cursor.execute(
            "INSERT INTO users (username, password, balance) VALUES (?, ?, ?)",
            (username, password, 0)
        )
        conn.commit()
        print("✅ Account created successfully!")
    except:
        print("❌ Username already exists!")


def login():
    print("\n--- Login ---")
    username = input("Username: ")
    password = input("Password: ")

    cursor.execute(
        "SELECT id, balance FROM users WHERE username=? AND password=?",
        (username, password)
    )
    result = cursor.fetchone()

    if result:
        print("✅ Login successful!")
        return result[0], result[1]
    else:
        print("❌ Invalid credentials!")
        return None, None


# ---------- BANK OPERATIONS ----------
def deposit(user_id, balance):
    amount = int(input("Enter deposit amount: "))
    balance += amount

    cursor.execute(
        "UPDATE users SET balance=? WHERE id=?",
        (balance, user_id)
    )

    cursor.execute(
        "INSERT INTO transactions (user_id, action, amount, date) VALUES (?, ?, ?, ?)",
        (user_id, "Deposit", amount, datetime.now())
    )

    conn.commit()
    print("💰 Deposit successful!")
    return balance


def withdraw(user_id, balance):
    amount = int(input("Enter withdraw amount: "))

    if amount > balance:
        print("❌ Insufficient balance!")
    else:
        balance -= amount
        cursor.execute(
            "UPDATE users SET balance=? WHERE id=?",
            (balance, user_id)
        )

        cursor.execut
