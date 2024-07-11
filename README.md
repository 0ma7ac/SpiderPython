SpiderPython
============

SpiderPython is a simple Python script that fetches all unique links from a given URL and prints the links that contain a specified keyword. This script uses the `requests` library to handle HTTP requests and the `BeautifulSoup` library to parse HTML content.

Features
--------
- Fetch all unique links from a webpage.
- Filter and print links containing a specified keyword.
- Disable SSL verification for ease of use with sites having SSL issues.

Prerequisites
-------------
- Python 3.x
- `requests` library
- `beautifulsoup4` library

You can install the required libraries using pip:

    pip install requests beautifulsoup4

Usage
-----
1. Clone this repository or download the script.

2. Open a terminal and navigate to the directory containing the script.

3. Run the script using Python:

    python main.py

4. When prompted, enter the URL of the webpage you want to scrape.

5. Enter the keyword you want to search for in the links.

6. The script will print all links containing the specified keyword.

Example
-------
    $ python main.py
    Enter the URL: https://example.com
    Enter the keyword: example

    Links containing the keyword:
    https://example.com/example-link1
    https://example.com/example-link2

