from page_urls import base_urls, sub_pages
from get_broken_links_list import get_broken_links
import urllib.parse

for site in base_urls:
    get_broken_links(site)
    
    for sub_page in sub_pages:
        site_category_page = urllib.parse.urljoin(site, sub_page)
        get_broken_links(site_category_page)

