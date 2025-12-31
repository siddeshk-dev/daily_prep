# Shopping Cart and Simple Banking System
cart = {}

while True:
    product = input("Enter product name (or exit): ")
    if product == "exit":
        break

    price = int(input("Enter price: "))
    cart[product] = price

print("\nShopping Cart:")
total = 0
for item in cart:
    print(item, ":", cart[item])
    total += cart[item]

print("Total Bill:", total)
accounts = {
    1001: 5000,
    1002: 8000,
    1003: 12000
}

acc_no = int(input("Enter account number: "))

if acc_no in accounts:
    print("Current Balance:", accounts[acc_no])
    withdraw = int(input("Enter withdraw amount: "))

    if withdraw <= accounts[acc_no]:
        accounts[acc_no] -= withdraw
        print("Withdrawal Successful")
        print("Remaining Balance:", accounts[acc_no])
    else:
        print("Insufficient Balance")
else:
    print("Account not found")
