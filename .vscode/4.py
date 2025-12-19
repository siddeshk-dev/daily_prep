def generate_username(name, year):
    username = name[:3].lower() + str(year)
    return username

name = input("Enter your name: ")
year = input("Enter birth year: ")

result = generate_username(name, year)
print("Your username is:", result)
students = {}

while True:
    name = input("Enter student name (or 'exit'): ")
    if name == "exit":
        break

    marks = int(input("Enter marks: "))
    students[name] = marks

print("\n--- Student List ---")
for s, m in students.items():
    print(s, "=>", m)
