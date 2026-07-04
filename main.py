import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")

def main():
    tasks = load_tasks()
    
    while True:
        print("\n--- MASTER TASK MANAGER ---")
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
                save_tasks(tasks)
                print(f"Added: {new_task}")
        elif choice == "2":
            if not tasks:
                print("No tasks to remove.")
                continue
            try:
                num = int(input("Enter task number to remove: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    save_tasks(tasks)
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

if __name__ == "__main__":
    main()