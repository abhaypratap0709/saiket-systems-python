# Basic Web Scraper

A simple console-based web scraper built with Python as part of the
**SaiKet Systems Python Development Internship – Task 4**.

The program fetches a user-provided URL and extracts the page title,
headings (h1–h3), and links.

## Features

- Fetches any public webpage via a user-entered URL
- Extracts and displays the page title
- Lists h1, h2, and h3 headings
- Lists links with their visible text and href
- Handles errors: invalid URL, connection failure, timeout, HTTP errors
- Sends a User-Agent header with each request

## Technologies / Libraries

- **requests** – HTTP GET requests
- **BeautifulSoup (bs4)** – HTML parsing
- **Python standard library** – input, loops, conditionals

## Installation

```bash
pip install requests beautifulsoup4
```

## How to Run

```bash
cd Task-4-Basic-Web-Scraper
python main.py
```

## Example Output

```
Welcome to the Basic Web Scraper!

===== Basic Web Scraper =====
1. Scrape a Website
2. Exit
=============================
Enter your choice: 1
Enter the URL to scrape: https://example.com
Fetching https://example.com ...

Page Title: Example Domain

Headings (1 found):
  [h1] Example Domain

Links (1 of 1 shown):
  More information...  →  https://www.iana.org/domains/example

===== Basic Web Scraper =====
1. Scrape a Website
2. Exit
=============================
Enter your choice: 2
Goodbye!
```

## What Was Learned

- How to send HTTP requests and handle responses with `requests`
- How to parse HTML and extract specific elements with BeautifulSoup
- How to handle network errors gracefully in Python
- Importance of setting a User-Agent header

## Limitations

- Only extracts title, headings, and links (no other content).
- Does not follow redirects across domains.
- Cannot scrape JavaScript-rendered pages.
- Link limit of 20 per page to keep output readable.
