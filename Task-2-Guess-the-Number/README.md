# Guess the Number Game

A console-based number guessing game built with Python as part of the
**SaiKet Systems Python Development Internship – Task 2**.

The program picks a random number between 1 and 100, and the player
tries to guess it with feedback after each attempt.

## Features

- Random number generation (1–100)
- Feedback on whether the guess is too high or too low
- Tracks and displays the number of attempts
- Input validation for non-numeric entries
- Option to play again after each round

## Concepts Used

- **Random module** – `random.randint()` for number generation
- **Loops** – `while True` for repeated guessing and replay
- **Conditional Statements** – `if/elif/else` for high/low/correct logic
- **Functions** – separate functions for input, game logic, and main flow
- **Input Validation** – rejects non-numeric input gracefully

## How to Run

> Python 3.6+ required. No external packages needed.

```bash
cd Task-2-Guess-the-Number
python main.py
```

## Example Output

```
Welcome to Guess the Number!

I have selected a number between 1 and 100.
Try to guess it!

Enter your guess: 50
Too high! Try again.

Enter your guess: 25
Too low! Try again.

Enter your guess: 37
Correct! You guessed the number in 3 attempt(s).

Play again? (y/n): n
Thanks for playing! Goodbye.
```

## Limitations

- No difficulty levels or configurable range.
- No persistent score history across sessions.
- Negative numbers are not explicitly handled (treated as too low).
