import json
from pathlib import Path

DATA_FILE = Path("tasks.json")

# ---------------------- Persistence helpers ----------------------

def load_tasks():
    """Load tasks from disk; return a list of strings."""
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            # If the file is corrupted, start fresh
            return []
    return []

def save_tasks(tasks):
    """Save tasks (list of strings) to disk."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

# ------------------------- App logic -----------------------------

def add_task(tasks, task):
    tasks.append(task)
    print(f"Added: {task}")

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet.")
        return
    print("\nYour tasks:")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")

def delete_task(tasks, index):
    """Delete a task by 1-based index."""
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        print(f"Deleted: {removed}")
    else:
        print("Invalid task number.")

if __name__ == "__main__":
    tasks = load_tasks()

    while True:
        print("\n1) Add Task  2) Show Tasks  3) Delete Task  4) Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            task = input("Enter task: ").strip()
            if task:
                add_task(tasks, task)
                save_tasks(tasks)  # persist after change
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks)
            try:
                idx = int(input("Task number to delete: "))
                delete_task(tasks, idx)
                save_tasks(tasks)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            save_tasks(tasks)
            print("Goodbye! Tasks saved.")
            break
        else:
            print("Invalid choice.")
