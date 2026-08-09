"""
Word Count Tool

A console-based text analysis tool that counts words,
characters, and lines in user-provided text.
"""


def display_menu():
    """Print the main menu."""
    print("\n===== Word Count Tool =====")
    print("1. Analyze Text")
    print("2. Exit")
    print("===========================")


def analyze_text(text):
    """Analyze the text and return a results dictionary."""
    words = text.split()
    lines = text.split("\n")
    char_count = len(text)
    char_no_spaces = len(text.replace(" ", ""))

    return {
        "words": len(words),
        "characters": char_count,
        "characters_no_spaces": char_no_spaces,
        "lines": len(lines),
    }


def display_results(results):
    """Print the analysis results."""
    print("\nWord Count Results")
    print("------------------")
    print(f"Words: {results['words']}")
    print(f"Characters: {results['characters']}")
    print(f"Characters (excluding spaces): {results['characters_no_spaces']}")
    print(f"Lines: {results['lines']}")


def get_text():
    """Prompt the user for text input."""
    text = input("Enter text: ")
    if not text.strip():
        print("Text cannot be empty. Please enter some text.")
        return None
    return text


def main():
    """Run the word count tool."""
    print("Welcome to the Word Count Tool!")

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            text = get_text()
            if text is not None:
                results = analyze_text(text)
                display_results(results)
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
