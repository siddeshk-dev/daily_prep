def get_balance():
    try:
        with open("balance.txt", "r") as f:
            return int(f.read())
    except:
        return 0

def save_balance(balance):
    with open("balance.txt", "w") as f:
        f.write(str(balance))

balance = get_balance()

while True:
    print("\n1.Deposit\n2.Withdraw\n3.Check Balance\n4.Exit")
    choice = input("Choice: ")

    if choice == "1":
        amt = int(input("Amount: "))
        balance += amt
        save_balance(balance)

    elif choice == "2":
        amt = int(input("Amount: "))
        if amt <= balance:
            balance -= amt
            save_balance(balance)
        else:
            print("Insufficient Balance")

    elif choice == "3":
        print("Balance:", balance)

    elif choice == "4":
        break
        print("Exiting... Goodbye!")
questions = {
    "Python is ___ language?": "interpreted",
    "Which keyword creates function?": "def",
    "Which symbol is used for comments?": "#"
}

score = 0
for q, a in questions.items():
    ans = input(q + " ")
    if ans.lower() == a:
        score += 1

print("Score:", score)
print("Thank you for playing!")
print("Goodbye!")