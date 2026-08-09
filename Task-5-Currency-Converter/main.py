"""
Currency Converter

A console-based multi-currency converter that fetches
live exchange rates from the ExchangeRate-API.
"""

import requests


API_URL = "https://open.er-api.com/v6/latest/{base}"
TIMEOUT = 10


def display_menu():
    """Print the main menu."""
    print("\n===== Currency Converter =====")
    print("1. Convert Currency")
    print("2. Exit")
    print("==============================")


def get_amount():
    """Prompt for an amount and validate it. Returns a float or None."""
    user_input = input("Enter amount: ").strip()
    if not user_input:
        print("Amount cannot be empty.")
        return None
    try:
        amount = float(user_input)
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return None
    if amount <= 0:
        print("Amount must be greater than zero.")
        return None
    return amount


def fetch_rates(base_currency):
    """Fetch exchange rates for the given base currency. Returns the rates dict or None."""
    url = API_URL.format(base=base_currency)
    try:
        response = requests.get(url, timeout=TIMEOUT)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect. Check your internet connection.")
        return None
    except requests.exceptions.Timeout:
        print("Error: The request timed out. Try again later.")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"Error: HTTP {e.response.status_code} – {e.response.reason}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

    if data.get("result") != "success":
        error_type = data.get("error-type", "")
        if error_type == "unsupported-code":
            print(f"Error: '{base_currency}' is not a supported currency code.")
            print("Please use a valid three-letter code such as USD, INR, EUR, or KRW.")
        else:
            print("Error: The API returned an unexpected response.")
        return None

    rates = data.get("rates")
    if not isinstance(rates, dict):
        print("Error: The API returned invalid exchange-rate data.")
        return None
    return rates


def convert_currency():
    """Ask the user for amount, source, and target currency, then convert."""
    amount = get_amount()
    if amount is None:
        return

    source = input("Enter source currency (e.g. USD): ").strip().upper()
    target = input("Enter target currency (e.g. INR): ").strip().upper()

    if not source or not target:
        print("Currency codes cannot be empty.")
        return

    print(f"Fetching exchange rates for {source} ...")
    rates = fetch_rates(source)
    if rates is None:
        return

    if target not in rates:
        print(f"Error: '{target}' is not a supported currency code.")
        return

    rate = rates[target]
    converted = amount * rate

    print(f"\n{amount:,.2f} {source} = {converted:,.2f} {target}")
    print(f"Exchange Rate: 1 {source} = {rate} {target}")


def main():
    """Run the currency converter application."""
    print("Welcome to the Currency Converter!")

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            convert_currency()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
