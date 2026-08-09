# Word Count Tool

A console-based text analysis tool built with Python as part of the
**SaiKet Systems Python Development Internship – Task 6**.

Analyzes user-provided text and reports word count, character count,
and line count.

## Features

- Count total words in the text
- Count total characters (with and without spaces)
- Count total lines
- Handles multiple spaces, leading/trailing whitespace correctly
- Input validation for empty text

## Technologies Used

- **Python 3.6+** (standard library only)

## How to Run

```bash
cd Task-6-Word-Count-Tool
python main.py
```

## Example Output

```
Welcome to the Word Count Tool!

===== Word Count Tool =====
1. Analyze Text
2. Exit
===========================
Enter your choice: 1
Enter text: Hello, world! How are you?

Word Count Results
------------------
Words: 5
Characters: 26
Characters (excluding spaces): 22
Lines: 1

===== Word Count Tool =====
1. Analyze Text
2. Exit
===========================
Enter your choice: 2
Goodbye!
```

## How Words Are Counted

Words are split using Python's `str.split()`, which splits on any whitespace
and automatically handles multiple spaces, tabs, and leading/trailing spaces.
Punctuation attached to a word (e.g. `world!`) is treated as part of that word.

## How Characters Are Counted

- **Characters** – total length of the input string, including spaces
- **Characters (excluding spaces)** – total length after removing all space characters

## Error Handling

- Empty or whitespace-only input is rejected with a clear message
- Invalid menu choices are handled gracefully

## Limitations

- Single-line input only (Python's `input()` reads one line at a time)
- Punctuation is counted as part of word characters
- Does not distinguish between types of whitespace in the exclusion count
