import random

def generate_link():
    characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    random_chars = ''.join(random.choice(characters) for _ in range(5)) #how many in extension EXAMPLE: https://random/hui2T
    link = "https://random/" + random_chars #base link
    return link

num_links = 100  # Number of links to generate

with open("urls.txt", "w") as file: #create txt file to store links generated
    for _ in range(num_links):
        link = generate_link()
        file.write(link + "\n")
        print(link)
