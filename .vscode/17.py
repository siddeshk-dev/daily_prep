tasks = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            print("\nYOUR TASKS:")
            if not tasks:
                print("No tasks yet!")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

        elif choice == '2':
            new_task = input("Enter the task: ")
            tasks.append(new_task)
            print("Task added!")

        elif choice == '3':
            if not tasks:
                print("Nothing to delete.")
                continue
            try:
                task_num = int(input("Enter task number to delete: "))
                removed = tasks.pop(task_num - 1)
                print(f"Removed: {removed}")
            except (ValueError, IndexError):
                print("Invalid number!")

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()