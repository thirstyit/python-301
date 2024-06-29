# Write a web scraper that fetches the information from the Wikipedia page
# on Web scraping. Extract all the links on the page and filter them so the
# navigation links are excluded.
# Programmatically follow one of the links that lead to another Wikipedia article,
# extract the text content from that article, and save it to a local text file.
# BONUS TASK: Use RegExp to find all numbers in the text.

import requests
from bs4 import BeautifulSoup
from pathlib import Path

URL = "https://en.wikipedia.org/wiki/Web_scraping"
output_path = Path("/Users/macintosh/Projects/python-301/04_web-scraping/")

response = requests.get(URL)

soup = BeautifulSoup(response.text)

body_text = soup.find("div", class_="mw-body-content")
link = body_text.find("a")

href_link = link["href"]

full_link = "https://en.wikipedia.org" + href_link

response2 = requests.get(full_link)



#for link in links:
#    print(link["href"] + "\n")








with open(output_path.joinpath("webpg.html"), "a") as file:
    file.write(response2.text)
    

          
