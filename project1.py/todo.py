import json
import os

FILE_NAME = 'todo.json'

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,'r') as file:
            return json.load(file)
    return []

#save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks,file,indent=4)


#add a new task
def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print("Task added.")
    else:
        print("Task cannot be empty.")
    save_tasks(tasks)

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\n your Tasks:")
        for idx, task in enumerate(tasks,start=1):
            print(f"{idx}. {task}")

# Delete a task

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_no = int(input("Enter the task number to delete: "))
        if 1 <= task_no <=len(tasks):
            removed = tasks.pop(task_no -1)
            print(f"Removed: {removed}")
            save_tasks(tasks)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


# Main menu loop

def main():
    tasks = load_tasks()
    while True:
        print("\n==== TO-DO LIST MENU ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. try again.")

if __name__ == '__main__':
    main()
