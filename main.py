import argparse
from pathlib import Path

DEFAULT_TASKS_FILENAME = "tasks.txt"

def load_tasks(tasks_file_path):
    if not tasks_file_path.exists():
        return []
    with tasks_file_path.open("r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks, tasks_file_path):
    tasks_file_path.parent.mkdir(parents=True, exist_ok=True)
    with tasks_file_path.open("w", encoding="utf-8") as file:
        for task in tasks:
            file.write(f"{task}\n")

def main(tasks_file_path):
    tasks = load_tasks(tasks_file_path)
    
    while True:
        print(f"\n--- MASTER TASK MANAGER ({tasks_file_path}) ---")
        if not tasks:
            print("[No pending tasks]")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        print("---------------------------")
        print("1. Add Task | 2. Remove Task | 3. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            new_task = input("Enter the new task: ").strip()
            if new_task:
                tasks.append(new_task)
                save_tasks(tasks, tasks_file_path)
                print(f"Added: {new_task}")
        elif choice == "2":
            if not tasks:
                print("No tasks to remove.")
                continue
            try:
                num = int(input("Enter task number to remove: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    save_tasks(tasks, tasks_file_path)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "3":
            print("Exiting application. Goodbye, Master.")
            break
        else:
            print("Invalid choice. Try again.")


def parse_args():
    parser = argparse.ArgumentParser(description="Simple task manager that can store tasks in another folder.")
    parser.add_argument(
        "--dir",
        dest="tasks_dir",
        default=".",
        help="Directory where tasks.txt will be stored. Defaults to current working directory.",
    )
    parser.add_argument(
        "--file",
        dest="tasks_file",
        default=None,
        help="Exact file path for the tasks file. Overrides --dir if provided.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    if args.tasks_file:
        tasks_file_path = Path(args.tasks_file).expanduser().resolve()
    else:
        tasks_file_path = Path(args.tasks_dir).expanduser().resolve() / DEFAULT_TASKS_FILENAME
    main(tasks_file_path)