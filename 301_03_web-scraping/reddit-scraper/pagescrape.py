import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.reddit.com/r/recipes/")
soup = BeautifulSoup(r.content, "html.parser")

links = soup.find_all("a")
print([l.text for l in links])