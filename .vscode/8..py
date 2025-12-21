students = {}

# ---------- PRINT HELPERS ----------
def line():
    print("=" * 60)

def header(title):
    line()
    print(title.center(60))
    line()

# ---------- SAFE INPUT ----------
def safe_int(message):
    while True:
        value = input(message)
        if value.isdigit():
            return int(value)
        else:
            print("❌ Enter numbers only!")

# ---------- CORE FUNCTIONS ----------
def add_student():
    header("ADD STUDENT")
    roll = input("Roll Number: ").strip()

    if roll in students:
        print("❌ Roll number already exists!")
        return

    name = input("Name: ").strip()
    marks = safe_int("Marks (0–100): ")

    students[roll] = {"name": name, "marks": marks}
    print("\n✅ Student added successfully!")

def view_students():
    header("STUDENT LIST")

    if not students:
        print("⚠ No students found.")
        return

    print(f"{'ROLL':<10}{'NAME':<30}{'MARKS':<10}")
    line()

    for roll, data in students.items():
        print(f"{roll:<10}{data['name']:<30}{data['marks']:<10}")

def search_student():
    header("SEARCH STUDENT")
    roll = input("Enter roll number: ")

    if roll in students:
        s = students[roll]
        print("\n✅ Student Found")
        print(f"Name  : {s['name']}")
        print(f"Marks : {s['marks']}")
    else:
        print("❌ Student not found!")

def result_report():
    header("RESULT REPORT")

    if not students:
        print("⚠ No data available.")
        return

    total = 0
    highest = -1
    topper = ""

    for s in students.values():
        total += s["marks"]
        if s["marks"] > highest:
            highest = s["marks"]
            topper = s["name"]

    average = total / len(students)

    print(f"Total Students : {len(students)}")
    print(f"Average Marks  : {average:.2f}")
    print(f"Topper        : {topper}")
    print(f"Highest Marks : {highest}")

def ranking():
    header("STUDENT RANKING")

    if not students:
        print("⚠ No students to rank.")
        return

    sorted_students = sorted(
        students.items(),
        key=lambda x: x[1]["marks"],
        reverse=True
    )

    print(f"{'RANK':<10}{'NAME':<30}{'MARKS':<10}")
    line()

    rank = 1
    for _, data in sorted_students:
        print(f"{rank:<10}{data['name']:<30}{data['marks']:<10}")
        rank += 1

# ---------- MAIN MENU ----------
def main_menu():
    while True:
        header("STUDENT MANAGEMENT SYSTEM")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Result Report")
        print("5. Ranking")
        print("6. Exit")
        line()

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            result_report()
        elif choice == "5":
            ranking()
        elif choice == "6":
            print("\n👋 Program exited safely. Thank you!")
            break
        else:
            print("❌ Invalid option!")

        input("\nPress ENTER to continue...")

# ---------- RUN ----------
main_menu()
