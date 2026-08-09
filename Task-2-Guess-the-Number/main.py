"""
Guess the Number Game

A console-based game where the player tries to guess
a randomly generated number between 1 and 100.
"""

import random


def get_guess():
    """Prompt the user for a guess and validate the input."""
    while True:
        user_input = input("Enter your guess: ").strip()
        if user_input.isdigit():
            return int(user_input)
        print("Invalid input. Please enter a valid number.")


def play_game():
    """Run one round of the guessing game."""
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nI have selected a number between 1 and 100.")
    print("Try to guess it!\n")

    while True:
        guess = get_guess()
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.\n")
        elif guess > secret_number:
            print("Too high! Try again.\n")
        else:
            print(f"Correct! You guessed the number in {attempts} attempt(s).\n")
            break


def main():
    """Start the game and offer to play again."""
    print("Welcome to Guess the Number!")

    while True:
        play_game()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()
