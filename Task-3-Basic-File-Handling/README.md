# Basic File Handling

A console application that demonstrates reading and writing text files,
built as part of the **SaiKet Systems Python Development Internship – Task 3**.

## Features

- Write user-provided text to `data.txt`
- Read and display the contents of `data.txt`
- Handles missing file with `FileNotFoundError`
- Validates empty input
- Menu-driven interface that runs until the user exits

## Concepts Used

- **File Handling** – `open()`, `read()`, `write()` with context managers
- **Error Handling** – `try/except` for `FileNotFoundError`
- **Functions** – separate functions for writing, reading, and menu display
- **Loops** – `while True` for continuous menu
- **Conditional Statements** – menu routing and input checks

## How to Run

> Python 3.6+ required. No external packages needed.

```bash
cd Task-3-Basic-File-Handling
python main.py
```

## Example Output

```
Welcome to the Basic File Handling App!

===== Basic File Handling =====
1. Write to File
2. Read from File
3. Exit
===============================
Enter your choice: 1
Enter text to save: Hello, this is my first file.
File saved successfully.

===== Basic File Handling =====
1. Write to File
2. Read from File
3. Exit
===============================
Enter your choice: 2

File Contents:
Hello, this is my first file.

===== Basic File Handling =====
1. Write to File
2. Read from File
3. Exit
===============================
Enter your choice: 3
Goodbye!
```

If `data.txt` does not exist:

```
Enter your choice: 2
Error: The file 'data.txt' was not found.
```

## Limitations

- Each write overwrites the previous content (does not append).
- Only works with a single file (`data.txt`).
- No support for multi-line input in one prompt.
