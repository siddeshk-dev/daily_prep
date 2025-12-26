list = ["apple", 3, "banana", 10, "cherry", 11, "date"]
print(list)
list[0]
print(list[0])
# 2×3 matrix
matrix = [
    [1, 9, 3],
    [4, 5, 9]
]
print(matrix[1][2])   # 2 (row 0, column 1)
name = "Siddesh k"
print(name[2:6:3])# out is
print(len(name))
name = input("Enter your name: ")
name2 = input("Enter your name: ")
message = input("Enter your message: ")
message2 = input("Enter your message: ")
print(f'{name} says "{message}"')
print(f' {name2} says "{message2}"')
x = 10
x *= 10
print(x) 
a = 5
b = 10
a, b = b, a
print(a, b)
word = "mango"
for i in range(len(word)):
    print(word[i], "is at index", i)
num = 7
print("Even" if num % 2 == 0 else "Odd")    
def add_book():
    name = input("Enter book name: ")
    author = input("Enter author name: ")
    year = input("Enter publication year: ")

    book = {
        "name": name,
        "author": author,
        "year": year
    }
    print("Book added!\n")

import random

print(" Welcome to the Number Guessing Game ")

play_again = "yes"

while play_again.lower() == "yes":
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("\nI have selected a number between 1 and 100.")
    print("Try to guess it!")

import random

print(" Welcome to the Number Guessing Game ")

while True:
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nI have selected a number between 1 and 100.")

    while True:
        guess = input("Enter your guess: ")

        # Input validation
        if not guess.isdigit():
            print(" Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret_number:
            print(" Too Low! Try again.")
        elif guess > secret_number:
            print(" Too High! Try again.")
        else:
            print("\n Correct! You guessed the number.")
            print(" Number:", secret_number)
            print(" Attempts:", attempts)
            break

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nThanks for playing! ")
        break
