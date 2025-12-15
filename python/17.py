# 🎨 Colorful ATM Program

# ANSI Color Codes
GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RESET = "\033[0m"

balance = 30000
pin = "1234"

print(BLUE + "=" * 45)
print("        🏦 PYTHON NATIONAL BANK")
print("=" * 45 + RESET)

entered_pin = input("🔐 Enter your 4-digit PIN: ")

if entered_pin != pin:
    print(RED + "\n❌ Incorrect PIN. Access Denied." + RESET)
else:
    while True:
        print(YELLOW + "\n" + "-" * 45)
        print("              MAIN MENU")
        print("-" * 45)
        print("1️⃣  Balance Enquiry")
        print("2️⃣  Deposit Money")
        print("3️⃣  Withdraw Money")
        print("4️⃣  Change PIN")
        print("5️⃣  Exit")
        print("-" * 45 + RESET)

        choice = input("👉 Choose option (1-5): ")

        # Balance
        if choice == "1":
            print(GREEN + f"\n💰 Available Balance: ₹{balance}" + RESET)

        # Deposit
        elif choice == "2":
            amount = input("💵 Enter deposit amount: ")

            if amount.isdigit():
                amount = int(amount)
                balance += amount
                print(GREEN + f"✅ ₹{amount} deposited successfully." + RESET)
            else:
                print(RED + "❌ Invalid amount." + RESET)

        # Withdraw
        elif choice == "3":
            amount = input("💸 Enter withdrawal amount: ")

            if not amount.isdigit():
                print(RED + "❌ Invalid amount." + RESET)
            else:
                amount = int(amount)
                if amount > balance:
                    print(RED + "❌ Insufficient balance." + RESET)
                else:
                    balance -= amount
                    print(GREEN + f"✅ ₹{amount} withdrawn successfully." + RESET)

        # Change PIN
        elif choice == "4":
            old_pin = input("🔑 Enter current PIN: ")

            if old_pin != pin:
                print(RED + "❌ Wrong PIN." + RESET)
            else:
                new_pin = input("🔐 Enter new 4-digit PIN: ")

                if new_pin.isdigit() and len(new_pin) == 4:
                    pin = new_pin
                    print(GREEN + "✅ PIN changed successfully." + RESET)
                else:
                    print(RED + "❌ PIN must be 4 digits." + RESET)

        # Exit
        elif choice == "5":
            print(BLUE + "\n🙏 Thank you for banking with Python National Bank!" + RESET)
            break

        else:
            print(RED + "❌ Invalid option. Try again." + RESET)
