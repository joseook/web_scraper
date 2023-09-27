
# Web Scraper for "Books to Scrape"

This project is a simple web scraper developed in Python to extract book information from the [Books to Scrape](http://books.toscrape.com/) website. It scrapes details such as title, price, availability, and book ratings.

## Requirements

- Python 3.x
- Libraries: `requests`, `bs4` (BeautifulSoup)

## Project Structure

```
web_scraper/
│
├── source/
│   ├── scraper/
│   │   └── scraper.py       # Functions related to web scraping
│   │
│   ├── logger/
│   │   └── logger.py        # Logging configurations
│   │
│   ├── config.py            # Constant configurations, such as base URL and User-Agents
│   └── main.py              # Main file for execution and user interaction
│
└── README.md                # Project documentation
```

## How to Use

1. **Dependency Installation**:
   First, install the required libraries using pip:
   ```
   pip install requests bs4
   ```

2. **Execution**:
   - Open the terminal or command prompt.
   - Navigate to the directory where the project files are located.
   - Run the `main.py` file:
     ```
     python source/main.py
     ```

3. **Interacting with the Script**:
   - The script will prompt you to enter the number of pages you wish to scrape. For example, type `2` to scrape the first two pages.
   - Next, it will ask for the output file name. You can press Enter to use the default (`books.csv`) or provide a different name.
   - The script will start scraping the data and display log messages indicating progress.

4. **Verification**:
   - After the script completes, check the output file in the same directory. It should contain the scraped data from the books.

## Notes

- This web scraper was developed for educational purposes.
- Always check the terms of service and the `robots.txt` file of a website before performing web scraping to ensure you have permission and are not violating any rules.

---