from pathlib import Path
import requests
from bs4 import BeautifulSoup


location = Path("/Users/martin/Documents/codingnomads/course-dev/python/labs/python-301/web-scraping/recipage.html")
BASE_URL = "https://www.reddit.com"
URL = f"{BASE_URL}/r/recipes/comments/m8p874/st_joseph_pastries_zeppole_di_san_giuseppe/"

def get_page_content(url):
    # Get the content
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}
    page = requests.get(url, headers=headers)
    return page

def get_content(url, testmode=False):
    if testmode:
        with open(url, "r") as fin:
            content = fin.read()
    else:
        content = get_page_content(url).text
    return content

def make_soup(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup

def get_comments(soup):
    comments = soup.find_all("div", class_="_3tw__eCCe7j-epNCKGXUKk")
    return comments

# breakpoint()

if __name__ == "__main__":
    html = get_content(location, testmode=True)
    soup = make_soup(html)
    print(type(soup))
    comments = get_comments(soup)

    for c in comments:
        user = c.find("div", class_="_2mHuuvyV9doV3zwbZPtIPG")#.text
        time = c.find("a", class_="_1sA-1jNHouHDpgCp1fCQ_F").text
        comment = c.find("div", class_="_3cjCphgls6DH-irkVaA0GM").text
        print(f"({user}: {time})\t[{comment}]")
