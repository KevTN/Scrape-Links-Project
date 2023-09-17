import requests
from bs4 import BeautifulSoup

def test_links_from_file(file_path):
    with open(file_path, "r") as file:
        links = file.read().splitlines()

    test_links(links)

def test_links(links):
    for link in links:
        try:
            response = requests.get(link)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                body_tag = soup.find("body")
                if body_tag and "display-page" in body_tag.get("class", []):
                    print(f"Link {link} is valid.")
                else:
                    print(f"Link {link} is invalid.")
            else:
                print(f"Link {link} returned a {response.status_code} error.")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while testing {link}: {e}")

# Example usage
file_path = "urls.txt"
test_links_from_file(file_path)
