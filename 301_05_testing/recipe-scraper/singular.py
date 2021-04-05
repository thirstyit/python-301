import requests
from bs4 import BeautifulSoup


URL = "https://codingnomads.github.io/recipes/recipes/68-kimchi-fried-rice-wi.html"

page = requests.get(URL)
soup = BeautifulSoup(page.text, "html.parser")
# print(soup.prettify())

# author = soup.find("p", class_="author").text.strip("by ")
author = soup.find("p", class_="author")
# recipe = soup.find("div", class_="md").text
print(author)
# print(recipe)
# print(soup.prettify())