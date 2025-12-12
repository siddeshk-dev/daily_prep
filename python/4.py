import os

FILENAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, " r ") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        for t in tasks:
            f.write(t + "\n")

def show_menu():
    print("\n===============================")
    print("         TO-DO MANAGER")
    print("===============================")
    print("1. View Tasks")
    print("2. Add Task")
# LONG PYTHON PRINTING PROGRAM – PATTERN 1
# LONG PYTHON PRINTING PROGRAM – PATTERN 1

print("Triangle Pattern\n")
for i in range(1, 21):
    print("*" * i)

print("\nSquare Pattern\n")
for i in range(10):
    print("#" * 25)

print("\nNumber Pyramid\n")
for i in range(1, 15):
    for j in range(1, i + 1):
        print(j, end="      ")
    print()

print("\nA–Z Letters\n")
for c in range(65, 91):
    print(chr(c), end="     ")


