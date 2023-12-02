import os

def display_menu():
    print("\n1. View Tasks")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Exit")

def view_tasks():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
        if tasks:
            print("\nTasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
        else:
            print("\nNo tasks found.")

def add_task():
    task = input("\nEnter task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully.")

def complete_task():
    view_tasks()
    try:
        task_number = int(input("\nEnter task number to mark as complete: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if 1 <= task_number <= len(tasks):
            completed_task = tasks.pop(task_number - 1)
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print(f"Task '{completed_task.strip()}' marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    if not os.path.exists("tasks.txt"):
        with open("tasks.txt", "w"):
            pass
    main()
