# Simple To-Do List Manager

import os

FILE_NAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def main():
    tasks = load_tasks()
    while True:
        print("\nOptions: [1] Add Task  [2] Complete Task  [3] Show Tasks  [4] Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            task = input("Enter a new task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added!")
        elif choice == "2":
            show_tasks(tasks)
            if tasks:
                idx = int(input("Enter task number to complete: "))
                if 1 <= idx <= len(tasks):
                    removed = tasks.pop(idx-1)
                    save_tasks(tasks)
                    print(f"Completed task: {removed}")
                else:
                    print("Invalid task number!")
        elif choice == "3":
            show_tasks(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
