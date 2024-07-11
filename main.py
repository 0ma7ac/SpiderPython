import requests
from urllib3.exceptions import InsecureRequestWarning
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# Suppress only the single InsecureRequestWarning from urllib3 needed
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def get_all_links(url):
    """
    Fetches all unique links from the given URL.

    Args:
        url (str): The URL of the webpage to scrape.

    Returns:
        set: A set of unique links found on the webpage.
    """
    try:
        # Send a GET request to the specified URL, ignoring SSL certificate errors
        response = requests.get(url, verify=False)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse the HTML content of the response
        soup = BeautifulSoup(response.text, 'html.parser')

        links = set()
        # Find all anchor tags with an href attribute
        for link in soup.find_all('a', href=True):
            href = link.get('href')
            # Check if the link is absolute
            if href.startswith(('http://', 'https://')):
                links.add(href)
            else:
                # Convert relative links to absolute links
                links.add(urljoin(url, href))

        return links
    except requests.RequestException as e:
        print(f"Request failed for {url}: {e}")
        return set()

def main():
    """
    Main function to run the script.
    Prompts the user for a URL and a keyword, then prints all links containing the keyword.
    """
    url = input("Enter the URL: ")
    keyword = input("Enter the keyword: ").lower()

    # Fetch all links from the provided URL
    links = get_all_links(url)

    print("\nLinks containing the keyword:")
    found_links = False
    # Filter links that contain the keyword
    for link in links:
        if keyword in link.lower():
            print(link)
            found_links = True

    if not found_links:
        print("No links containing the keyword were found.")

if __name__ == "__main__":
    main()
