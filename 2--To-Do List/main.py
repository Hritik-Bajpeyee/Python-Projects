# To-Do List
# Create a command-line app to manage tasks (add, remove, mark as complete).
# Store tasks in a text file for persistence.


import os

Task_FILE = "tasks.txt"

def load_task():
    if not os.path.exists(Task_FILE):
        with open(Task_FILE, "w") as f:
            pass
    with open(Task_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(Task_FILE, 'w') as f:
        f.write("\n".join(tasks))

def list_task(tasks):
    print("Tasks: ")
    if not tasks:
        print("\nNo tasks Found!")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def add_task(tasks):
    task_name = input("Enter The Task: ")
    tasks.append(f"[ ] {task_name}")
    save_tasks(tasks)
    print("Task Added \n")

def remove_task(tasks):
    list_task(tasks)
    try:
        task_no = int(input("Enter The Task Number to Remove: ")) - 1
        if 0 <= task_no < len(tasks):
            removed = tasks.pop(task_no)
            save_tasks(tasks)
            print(f"Removed task: {removed}\n")
        else:
            print("Invalid Task Number!!\n")
    except ValueError:
        print("Please Enter a Valid Number!")

def mark_task(tasks):
    list_task(tasks)
    try:
        task_no = int(input("Enter The Task Number To Mark As Complete: ")) - 1
        if 0 <= task_no < len(tasks):
            if tasks[task_no].startswith("[ ]"):
                tasks[task_no] = tasks[task_no].replace("[ ]", "[#]", 1)
                save_tasks(tasks)
                print("Task Marked Successfully!\n")
            else:
                print("Task Already marked!!\n")
        else:
            print("Invalid Task Number.\n")
    except ValueError:
        print("Please enter a valid number!\n")

def remove_mark_task(tasks):
    list_task(tasks)
    try:
        task_no = int(input("Enter The Task Number To Remove Mark: ")) - 1
        if 0 <= task_no < len(tasks):
            if tasks[task_no].startswith("[#]"):
                tasks[task_no] = tasks[task_no].replace("[#]", "[ ]", 1)
                save_tasks(tasks)
                print("Task Unmarked Successfully!\n")
            else:
                print("Task is not marked!!\n")
        else:
            print("Invalid Task Number.\n")
    except ValueError:
        print("Please enter a valid number!\n")

def main():
    tasks = load_task()
    while True:
        print("Task Manager")
        print("1. List Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task As Complete")
        print("5. Remove Mark from Task")
        print("6. Exit")

        choice = input("Choose Your option: ")
        if choice == "1":
            list_task(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            mark_task(tasks)
        elif choice == "5":
            remove_mark_task(tasks)
        elif choice == "6":
            print("Exiting.....")
            break
        else:
            print("Invalid Option")

if __name__ == "__main__":
    main()
