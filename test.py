# Task Manager Application

def display_menu():
    print("\n--- Task Manager Menu ---")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Mark task as complete")
    print("4. Delete a task")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found. You are all caught up!")
        return
    
    print("\n--- Your Tasks ---")
    for index, task in enumerate(tasks):
        status = "[X]" if task['completed'] else "[ ]"
        print(f"{index + 1}. {status} {task['name']}")

def add_task(tasks):
    task_name = input("\nEnter the new task: ").strip()
    if task_name:
        tasks.append({"name": task_name, "completed": False})
        print(f"Task '{task_name}' added successfully.")
    else:
        print("Task name cannot be empty.")

def complete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    
    try:
        task_num = int(input("\nEnter task number to mark complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['completed'] = True
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    
    try:
        task_num = int(input("\nEnter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Task '{removed['name']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    print("Welcome to the Task Manager!")
    
    while True:
        display_menu()
        choice = input("\nChoose an option (1-5): ").strip()
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("\nExiting Task Manager. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please pick a number from 1 to 5.")

if __name__ == "__main__":
    main()