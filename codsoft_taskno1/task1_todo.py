import json
import os

TODO_FILE = "todos.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def show_tasks(tasks):
    if not tasks:
        print("\n  No tasks found!")
        return
    print("\n  ╔══════════════════════════════════════╗")
    print("  ║           YOUR TO-DO LIST            ║")
    print("  ╠══════════════════════════════════════╣")
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["done"] else "○"
        label = "[DONE]" if task["done"] else "      "
        print(f"  ║  {i}. [{status}] {label} {task['title'][:25]:<25}║")
    print("  ╚══════════════════════════════════════╝")

def add_task(tasks):
    title = input("\n  Enter task: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print(f"  ✔ Task '{title}' added!")
    else:
        print("  Task cannot be empty.")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        num = int(input("\n  Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            save_tasks(tasks)
            print(f"  ✔ Task '{tasks[num-1]['title']}' marked as done!")
        else:
            print("  Invalid number.")
    except ValueError:
        print("  Please enter a valid number.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("\n  Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"  ✔ Task '{removed['title']}' deleted!")
        else:
            print("  Invalid number.")
    except ValueError:
        print("  Please enter a valid number.")

def update_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("\n  Enter task number to update: "))
        if 1 <= num <= len(tasks):
            new_title = input(f"  New title for '{tasks[num-1]['title']}': ").strip()
            if new_title:
                tasks[num - 1]["title"] = new_title
                save_tasks(tasks)
                print("  ✔ Task updated!")
        else:
            print("  Invalid number.")
    except ValueError:
        print("  Please enter a valid number.")

def main():
    print("\n  ====================================")
    print("       CODSOFT - TO-DO LIST APP      ")
    print("  ====================================")
    tasks = load_tasks()

    while True:
        print("\n  MENU:")
        print("  1. View Tasks")
        print("  2. Add Task")
        print("  3. Mark as Done")
        print("  4. Update Task")
        print("  5. Delete Task")
        print("  6. Exit")

        choice = input("\n  Choose an option (1-6): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            update_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("\n  Goodbye! Stay productive! 👋\n")
            break
        else:
            print("  Invalid choice. Please enter 1-6.")

if __name__ == "__main__":
    main()
