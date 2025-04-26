# task_manager.py

def show_tasks():
    try:
        with open("tasks.txt", "r", encoding="utf-8") as file:
            tasks = file.readlines()
            if tasks:
                print("\nCurrent tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
            else:
                print("\nNo tasks available.")
    except FileNotFoundError:
        print("\nTask file not found. It will be created when you add a new task.")

def add_task():
    task = input("Enter a new task: ")
    with open("tasks.txt", "a", encoding="utf-8") as file:
        file.write(task + "\n")
    print("Task added successfully!")

def delete_task():
    show_tasks()
    try:
        task_num = int(input("Enter the number of the task you want to delete: "))
        with open("tasks.txt", "r", encoding="utf-8") as file:
            tasks = file.readlines()

        if 0 < task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            with open("tasks.txt", "w", encoding="utf-8") as file:
                file.writelines(tasks)
            print(f"Task deleted: {removed.strip()}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    except FileNotFoundError:
        print("Task file not found.")

def main_menu():
    while True:
        print("\n--- Task Manager ---")
        print("1. Show tasks")
        print("2. Add a task")
        print("3. Delete a task")
        print("4. Exit")

        choice = input("Please select a number: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if name == "main":
    main_menu()