"""
Basic Web Scraper

A console-based web scraper that fetches a webpage and
extracts its title, headings, and links using requests
and BeautifulSoup.
"""

import requests
from bs4 import BeautifulSoup


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}
TIMEOUT = 10


def display_menu():
    """Print the main menu."""
    print("\n===== Basic Web Scraper =====")
    print("1. Scrape a Website")
    print("2. Exit")
    print("=============================")


def fetch_page(url):
    """Send a GET request and return the Response object, or None on error."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        response.raise_for_status()
        return response
    except requests.exceptions.MissingSchema:
        print("Error: Invalid URL. Make sure it starts with http:// or https://")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect. Check the URL or your internet connection.")
    except requests.exceptions.Timeout:
        print("Error: The request timed out. Try again later.")
    except requests.exceptions.HTTPError as e:
        print(f"Error: HTTP {e.response.status_code} – {e.response.reason}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    return None


def display_title(soup):
    """Print the page title if available."""
    title = soup.title
    if title and title.string:
        print(f"\nPage Title: {title.string.strip()}")
    else:
        print("\nPage Title: (not found)")


def display_headings(soup):
    """Print h1, h2, and h3 headings if any are found."""
    headings = soup.find_all(["h1", "h2", "h3"])
    if not headings:
        print("\nHeadings: None found.")
        return
    print(f"\nHeadings ({len(headings)} found):")
    for tag in headings:
        text = tag.get_text(strip=True)
        if text:
            print(f"  [{tag.name}] {text}")


def display_links(soup, limit=20):
    """Print anchor tags showing visible text and href."""
    links = soup.find_all("a", href=True)
    if not links:
        print("\nLinks: None found.")
        return
    shown = min(len(links), limit)
    print(f"\nLinks ({shown} of {len(links)} shown):")
    for link in links[:limit]:
        text = link.get_text(strip=True) or "(no text)"
        href = link["href"]
        print(f"  {text}  →  {href}")


def scrape_website():
    """Prompt for a URL, fetch the page, and display extracted data."""
    url = input("Enter the URL to scrape: ").strip()
    if not url:
        print("URL cannot be empty.")
        return

    print(f"Fetching {url} ...")
    response = fetch_page(url)
    if response is None:
        return

    soup = BeautifulSoup(response.text, "html.parser")
    display_title(soup)
    display_headings(soup)
    display_links(soup)


def main():
    """Run the web scraper application."""
    print("Welcome to the Basic Web Scraper!")

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            scrape_website()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
