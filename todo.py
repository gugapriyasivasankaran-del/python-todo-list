"""Simple command-line to-do list. Tasks are saved in tasks.json."""
import json
import os

FILE = "tasks.json"


def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for i, t in enumerate(tasks, start=1):
        mark = "x" if t["done"] else " "
        print(f"{i}. [{mark}] {t['title']}")


def main():
    tasks = load_tasks()
    while True:
        print("\n1. View  2. Add  3. Complete  4. Delete  5. Quit")
        choice = input("Choose: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            title = input("Task: ").strip()
            if title:
                tasks.append({"title": title, "done": False})
                save_tasks(tasks)
                print("Added.")
        elif choice in ("3", "4"):
            show_tasks(tasks)
            try:
                n = int(input("Task number: ")) - 1
                if choice == "3":
                    tasks[n]["done"] = True
                    print("Marked as done.")
                else:
                    tasks.pop(n)
                    print("Deleted.")
                save_tasks(tasks)
            except (ValueError, IndexError):
                print("Invalid task number.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Please choose 1-5.")


if __name__ == "__main__":
    main()
