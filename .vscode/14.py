password = input("Enter password: ")

if len(password) < 6:
    print("Weak Password ❌")
elif any(char.isdigit() for char in password) and any(char.isupper() for char in password):
    print("Strong Password ✅")
else:
    print("Medium Password ⚠️")


import random

secret = random.randint(1, 10)

while True:
    guess = int(input("Guess number (1-10): "))
    if guess == secret:
        print("Correct! 🎉")
        break
    else:
        print("Try again")


student = {}

for i in range(3):
    subject = input("Enter subject: ")
    marks = int(input("Enter marks: "))
    student[subject] = marks

total = sum(student.values())
avg = total / len(student)

print("\nReport Card")
print(student)
print("Total:", total)
print("Average:", avg)


balance = 1000

def deposit(amount):
    global balance
    balance += amount

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
    else:
        print("Insufficient Balance")

deposit(500)
withdraw(300)

print("Final Balance:", balance)
