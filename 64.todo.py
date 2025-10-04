# Simple To-Do List using Python

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks in your to-do list.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "✔" if task['completed'] else "✖"
            print(f"{i}. [{status}] {task['name']}")
    print()

def add_task():
    task_name = input("Enter the task name: ")
    tasks.append({"name": task_name, "completed": False})
    print(f"Task '{task_name}' added.\n")

def complete_task():
    show_tasks()
    if tasks:
        try:
            task_number = int(input("Enter the task number to mark as complete: "))
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]['completed'] = True
                print(f"Task '{tasks[task_number - 1]['name']}' marked as complete.\n")
            else:
                print("Invalid task number.\n")
        except ValueError:
            print("Please enter a valid number.\n")

while True:
    print("To-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    print()
    
    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        complete_task()
    elif choice == '4':
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1-4.\n")
