"""
Basic File Handling

A console application that demonstrates writing to
and reading from a text file with error handling.
"""

FILENAME = "data.txt"


def display_menu():
    """Print the main menu."""
    print("\n===== Basic File Handling =====")
    print("1. Write to File")
    print("2. Read from File")
    print("3. Exit")
    print("===============================")


def write_to_file():
    """Ask the user for text and write it to the data file."""
    text = input("Enter text to save: ").strip()
    if not text:
        print("Nothing to save. Please enter some text.")
        return
    with open(FILENAME, "w") as file:
        file.write(text)
    print("File saved successfully.")


def read_from_file():
    """Read and display the contents of the data file."""
    try:
        with open(FILENAME, "r") as file:
            contents = file.read()
        if contents:
            print(f"\nFile Contents:\n{contents}")
        else:
            print("The file is empty.")
    except FileNotFoundError:
        print(f"Error: The file '{FILENAME}' was not found.")


def main():
    """Run the file handling application."""
    print("Welcome to the Basic File Handling App!")

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            write_to_file()
        elif choice == "2":
            read_from_file()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
