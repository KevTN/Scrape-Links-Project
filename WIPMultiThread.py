import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

def test_link(link):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            body_tag = soup.find("body")
            if body_tag and "display-page" in body_tag.get("class", []):
                return f"Link {link} is valid."
            else:
                return f"Link {link} is invalid."
        else:
            return f"Link {link} returned a {response.status_code} error."
    except requests.exceptions.RequestException as e:
        return f"An error occurred while testing {link}: {e}"

def test_links_from_file(file_path):
    with open(file_path, "r") as file:
        links = file.read().splitlines()

    with ThreadPoolExecutor(max_workers = 5) as executor:  # Adjust max_workers as needed
        results = list(executor.map(test_link, links))

    for result in results:
        print(result)

# Example usage
file_path = "urls.txt"
test_links_from_file(file_path)