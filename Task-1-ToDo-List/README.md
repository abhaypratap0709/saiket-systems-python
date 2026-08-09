# To-Do List Application

A simple console-based to-do list manager built with Python as part of the
**SaiKet Systems Python Development Internship – Task 1**.

## Features

- Add tasks with a description
- View all tasks with their status (Pending / Done)
- Mark tasks as completed
- Input validation and error handling
- Runs in a loop until the user exits

## Concepts Used

- **Dictionaries** – each task is a `dict` with `description` and `completed` keys
- **Lists** – all tasks are stored in a list
- **Functions** – separate function for each action
- **Conditional Statements** – menu routing and validation
- **Loops** – `while True` keeps the app running

## How to Run

> Python 3.6+ required. No external packages needed.

```bash
cd Task-1-ToDo-List
python main.py
```

## Example Output

```
Welcome to the To-Do List Application!

===== To-Do List =====
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Exit
======================
Choose an option (1-4): 1
Enter task description: Buy groceries
Task "Buy groceries" added successfully!

===== To-Do List =====
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Exit
======================
Choose an option (1-4): 2

----- Your Tasks -----
  1. [Pending] Buy groceries
----------------------

===== To-Do List =====
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Exit
======================
Choose an option (1-4): 3

----- Your Tasks -----
  1. [Pending] Buy groceries
----------------------
Enter the task number to mark as completed: 1
Task "Buy groceries" marked as completed!

===== To-Do List =====
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Exit
======================
Choose an option (1-4): 4
Thank you for using the To-Do List. Goodbye!
```

## Limitations

- Tasks are stored in memory only; they are lost when the program exits.
- No option to edit or delete a task.
- No priority or due-date support.
