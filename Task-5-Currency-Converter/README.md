# Currency Converter

A console-based multi-currency converter built with Python as part of the
**SaiKet Systems Python Development Internship – Task 5**.

Fetches live exchange rates from a free API and converts between any
two supported currencies.

## Features

- Convert between 160+ currencies using live exchange rates
- Accepts currency codes in any case (e.g. `usd`, `USD`)
- Displays original amount, converted amount, and exchange rate
- Handles invalid input, network errors, and unsupported currencies

## Technologies Used

- **Python 3.6+**
- **requests** – HTTP requests to the exchange-rate API

## API Used

**ExchangeRate-API** (free tier, no API key required)

- Endpoint: `https://open.er-api.com/v6/latest/{base_currency}`
- Returns a JSON object with a `rates` dictionary mapping currency codes to
  their exchange rates relative to the base currency.
- Rates are updated daily.

Example request:
```
GET https://open.er-api.com/v6/latest/USD
```

Example response (abbreviated):
```json
{
  "result": "success",
  "base_code": "USD",
  "rates": {
    "USD": 1,
    "INR": 95.25,
    "EUR": 0.866,
    "GBP": 0.742
  }
}
```

## Installation

```bash
pip install requests
```

## How to Run

```bash
cd Task-5-Currency-Converter
python main.py
```

## Example Output

```
Welcome to the Currency Converter!

===== Currency Converter =====
1. Convert Currency
2. Exit
==============================
Enter your choice: 1
Enter amount: 100
Enter source currency (e.g. USD): USD
Enter target currency (e.g. INR): INR
Fetching exchange rates for USD ...

100.00 USD = 9,524.92 INR
Exchange Rate: 1 USD = 95.249248 INR

===== Currency Converter =====
1. Convert Currency
2. Exit
==============================
Enter your choice: 2
Goodbye!
```

## Error Handling

- Empty, non-numeric, zero, or negative amounts are rejected
- Invalid or unsupported currency codes produce a clear message
- Network errors, timeouts, and HTTP errors are caught and reported
- The program always returns to the menu after an error

## Limitations

- Requires an internet connection.
- Exchange rates are updated once per day by the API.
- Does not store conversion history.
- Does not list all available currency codes.
