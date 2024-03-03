tasks = []

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")

def remove_task():
    if len(tasks) == 0:
        print("No tasks to remove.")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")
        choice = int(input("Enter the number of the task to remove: "))
        if choice >= 1 and choice <= len(tasks):
            removed_task = tasks.pop(choice - 1)
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print("Invalid choice.")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks.")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")

while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        remove_task()
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
