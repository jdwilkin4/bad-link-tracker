from bs4 import BeautifulSoup

import requests
from requests.exceptions import ConnectionError

import urllib.parse

# url = input("Enter your url: ")
url = "https://angular.framework.dev/"
page = requests.get(url)
response_code = str(page.status_code)
data = page.text
soup = BeautifulSoup(data, features="html.parser")
num_broken_img_links = 0
broken_links_list = []

for img in soup.find_all('img'):
    original_img_url = img.get('src')

    if not original_img_url.startswith("http"):
        original_img_url = urllib.parse.urljoin(page.url, original_img_url)
    
    try:
         img_url = requests.get(original_img_url)
    except ConnectionError:
        num_broken_img_links = num_broken_img_links + 1
        broken_links_list.append(original_img_url)
    else:
        img_url_response_code = img_url.status_code

        if img_url_response_code != 200:
            num_broken_img_links = num_broken_img_links + 1
            broken_links_list.append(original_img_url)
            # print(f"Url: {original_img_url} " + f"| Status Code: {img_url_response_code}")
           
  

if num_broken_img_links == 0:
    print("No broken links found")
else:
    print(broken_links_list)

