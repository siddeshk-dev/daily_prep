password = input("Enter password: ")

if len(password) >= 8 and password.isalnum():
    print("Strong password")
else:
    print("Weak password")
choice = int(input("Enter a number (1-3): "))

match choice:
    case 1:
        print("You chose Python")
    case 2:
        print("You chose Java")
    case 3:
        print("You chose JavaScript")
    case _:
        print("Invalid choice")

 
add = lambda a, b: a + b
mul = lambda a, b: a * b
print("Add:", add(5, 3))
print("Multiply:", mul(4, 6))


