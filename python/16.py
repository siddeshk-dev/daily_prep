# Real Bank-Style ATM Program

balance = 25000
pin = "1234"

print("=" * 1)
print("        🏦 PYTHON NATIONAL BANK")
print("=" * 1)

entered_pin = input("Enter your 4-digit PIN: ")

if entered_pin != pin:
    print("\n❌ Incorrect PIN. Access Denied.")
else:
    while True:
        print("\n" + "-" * 1)
        print("         ATM MAIN MENU")
        print("-" * 1)
        print("1. Check Balance")
        print("2. Deposit Money")   
        print("3. Withdraw Money")
        print("4. Exit")
        choice = input("Select an option (1-4): ")
# ATM Program with File Storage

FILE_NAME = "bank_data.txt"

# Create file if not exists
try:
    with open(FILE_NAME, "r") as f:
        pin, balance = f.read().split(",")
        balance = int(balance)
except:
    pin = "1234"
    balance = 20000
    with open(FILE_NAME, "w") as f:
        f.write(f"{pin},{balance}")

print("=" * 45)
print("        🏦 PYTHON NATIONAL BANK")
print("=" * 45)

entered_pin = input("Enter your 4-digit PIN: ")
