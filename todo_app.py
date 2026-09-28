"""
To-Do List Application
Author: Jeffrey Antwi
Date: 24th September 2026
Purpose: A simple command-line to-do list manager demonstrating Python fundamentals
"""

def display_menu():
    """Display the main menu options."""
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Exit")
    print("===========================")


# Feature: Allow users to create new tasks with input validation
def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter task description: ").strip()
    if task:
        tasks.append({"description": task, "completed": False})
        print(f"Task '{task}' added successfully!")
    else:
        print("Task cannot be empty.")

# Feature: Display all tasks with completion status indicators

def view_tasks(tasks):
    """Display all tasks with their status."""
    if not tasks:
        print("\nNo tasks found.")
        return
    
    print("\n----- YOUR TASKS -----")
    for index, task in enumerate(tasks, start=1):
        status = "✓ DONE" if task["completed"] else "○ TODO"
        print(f"{index}. [{status}] {task['description']}")
    print("----------------------")

# Feature: Mark tasks as completed with error handling

def mark_complete(tasks):
    """Mark a specific task as completed."""
    if not tasks:
        print("No tasks to mark complete.")
        return
    
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to mark complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print(f"Task {task_num} marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Feature: Remove tasks from list with confirmation

def delete_task(tasks):
    """Remove a task from the list."""
    if not tasks:
        print("No tasks to delete.")
        return
    
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Task '{removed['description']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    """Main function to run the to-do list application."""
    tasks = []  # List to store task dictionaries
    print("Welcome to your To-Do List!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()