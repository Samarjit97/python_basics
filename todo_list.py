# Simple To-Do List App

tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def show_tasks():
    print("\nYour tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

if __name__ == "__main__":
    while True:
        print("\n1. Add Task\n2. Show Tasks\n3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
