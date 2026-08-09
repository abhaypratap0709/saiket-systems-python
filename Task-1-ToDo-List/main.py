"""
To-Do List Application

A simple console-based to-do list manager.
Tasks are stored as a list of dictionaries, each with a 'description'
and 'completed' key.

Author : Abhay Kumar Singh
Task   : SaiKet Systems Internship – Task 1
"""


def display_menu():
    """Print the main menu."""
    print("\n===== To-Do List =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")
    print("======================")


def add_task(tasks):
    """Prompt the user for a description and add a new task."""
    description = input("Enter task description: ").strip()
    if not description:
        print("Task description cannot be empty. Please try again.")
        return
    tasks.append({"description": description, "completed": False})
    print(f'Task "{description}" added successfully!')


def view_tasks(tasks):
    """Display all tasks with their number and status."""
    if not tasks:
        print("No tasks found. Your to-do list is empty.")
        return
    print("\n----- Your Tasks -----")
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"  {index}. [{status}] {task['description']}")
    print("----------------------")


def mark_task_completed(tasks):
    """Mark a task as completed by its number."""
    if not tasks:
        print("No tasks to mark. Add some tasks first.")
        return

    view_tasks(tasks)

    choice = input("Enter the task number to mark as completed: ").strip()
    if not choice.isdigit():
        print("Invalid input. Please enter a valid task number.")
        return

    task_number = int(choice)
    if task_number < 1 or task_number > len(tasks):
        print(f"Invalid task number. Please choose between 1 and {len(tasks)}.")
        return

    task = tasks[task_number - 1]
    if task["completed"]:
        print(f'Task "{task["description"]}" is already marked as completed.')
    else:
        task["completed"] = True
        print(f'Task "{task["description"]}" marked as completed!')


def main():
    """Run the to-do list application."""
    tasks = []
    print("Welcome to the To-Do List Application!")

    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            print("Thank you for using the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
