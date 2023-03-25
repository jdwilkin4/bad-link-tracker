from bs4 import BeautifulSoup
import requests
from requests.exceptions import ConnectionError
import urllib.parse


def get_broken_links(site):
    page = requests.get(site)
    data = page.text
    soup = BeautifulSoup(data, features="html.parser")
    num_broken_img_links = 0
    broken_links_list = []
 

    for img in soup.find_all('img'):
        img_url = img.get('src')

        if not img_url.startswith("http"):
            img_url = urllib.parse.urljoin(page.url, img_url)
        
        try:
            img_url = requests.get(img_url)
        except ConnectionError:
            num_broken_img_links = num_broken_img_links + 1
            broken_links_list.append(img_url)
        else:
            if img_url.status_code != 200:
                num_broken_img_links = num_broken_img_links + 1
                broken_links_list.append(img_url)
            
    

    if num_broken_img_links == 0:
        print("no broken links")
        return
    else:
        print(broken_links_list)
        return broken_links_list

