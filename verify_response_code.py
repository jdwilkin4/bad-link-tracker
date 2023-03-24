from bs4 import BeautifulSoup

import requests

url = input("Enter your url: ")
page = requests.get(url)
response_code = str(page.status_code)
data = page.text
soup = BeautifulSoup(data, features="html.parser")
num_broken_img_links = 0

for img in soup.find_all('img'):
    original_img_url = img.get('src')
    img_url = (requests.get(original_img_url)).url
    img_url_response_code = requests.get(img_url).status_code
    history = requests.get(original_img_url).history

    if img_url_response_code != 200:
        num_broken_img_links = num_broken_img_links + 1
        print(f"Url: { original_img_url} " + f"| Status Code: {img_url_response_code}")

    if original_img_url == "https://www.primefaces.org/primeng/assets/showcase/images/primeng-logo-dark.svg":
        print("this is the history for broken angular img " + f"{history}")
        # TODO: add loop to print urls for history

if num_broken_img_links == 0:
    print("No broken links found")