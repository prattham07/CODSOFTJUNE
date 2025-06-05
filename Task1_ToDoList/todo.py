tasks = []

def show_tasks():
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added.")

def remove_task():
    show_tasks()
    task_no = int(input("Enter task number to remove: "))
    if 0 < task_no <= len(tasks):
        removed = tasks.pop(task_no - 1)
        print(f"Removed task: {removed}")
    else:
        print("Invalid task number.")

while True:
    print("\nOptions: 1.Add  2.Show  3.Remove  4.Exit")
    choice = input("Choose: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        break
    else:
        print("Invalid option.")