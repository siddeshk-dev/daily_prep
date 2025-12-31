# Smart Activity Tracker with Decorators, Context Managers, Dataclasses, and Generators
from dataclasses import dataclass
from datetime import datetime
import time

# ---------------- DECORATOR ----------------
def activity_logger(func):
    def wrapper(*args, **kwargs):
        print("\n🔹 Activity started...")
        result = func(*args, **kwargs)
        print("🔹 Activity finished.\n")
        return result
    return wrapper


# ---------------- CONTEXT MANAGER ----------------
class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "a+")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


# ---------------- DATACLASS ----------------
@dataclass
class Activity:
    name: str
    duration: int
    timestamp: str


# ---------------- GENERATOR ----------------
def activity_generator(activities):
    for act in activities:
        yield act


# ---------------- CORE SYSTEM ----------------
class SmartTracker:
    def __init__(self):
        self.activities = []

    @activity_logger
    def add_activity(self):
        name = input("Enter activity name: ")
        duration = int(input("Enter duration (minutes): "))
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        activity = Activity(name, duration, time_now)
        self.activities.append(activity)

        with FileManager("activities.txt") as file:
            file.write(f"{activity}\n")

        print(" Activity saved successfully!")

    @activity_logger
    def show_activities(self):
        if not self.activities:
            print("⚠ No activities recorded yet.")
            return

        print("\n Your Activities:\n")
        for act in activity_generator(self.activities):
            print(f" {act.name} |  {act.duration} min |  {act.timestamp}")

    @activity_logger
    def read_from_file(self):
        print("\n Activity History from File:\n")
        try:
            with open("activities.txt", "r") as file:
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print(" No file found yet.")


# ---------------- MAIN MENU ----------------
def main():
    tracker = SmartTracker()

    while True:
        print("""
==============================
 SMART ACTIVITY TRACKER
==============================
1. Add Activity
2. Show Activities
3. Read Activities from File
4. Exit
""")
        choice = input("Choose option: ")

        if choice == "1":
            tracker.add_activity()
        elif choice == "2":
            tracker.show_activities()
        elif choice == "3":
            tracker.read_from_file()
        elif choice == "4":
            print(" Exiting program. Stay productive!")
            break
        else:
            print(" Invalid choice. Try again.")


# ---------------- RUN ----------------
if __name__ == "__main__":
    main()

