
balance = 10000
correct_pin = "1234"

print(" Welcome to Python ATM")

# PIN Verification
pin = input("Enter your 4-digit PIN: ")

if pin != correct_pin:
    print(" Wrong PIN. Access Denied.")
else:
    while True:
        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")