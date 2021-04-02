import unittest
from pathlib import Path
import redcipe


class TestScraper(unittest.TestCase):

    def setUp(self):
        BASE_URL = "https://www.reddit.com"
        URL = f"{BASE_URL}/r/recipes/comments/m8p874/st_joseph_pastries_zeppole_di_san_giuseppe/"
        location = Path("/Users/martin/Documents/codingnomads/course-dev/python/labs/python-301/web-scraping/recipage.html")
        self.url = URL
        self.location = location

    def test_get_valid_html_response(self):
        page = redcipe.get_page_content(self.url)
        self.assertEqual(page.status_code, 200)

    def test_get_content_returns_html_string(self):
        html_cached = redcipe.get_content(self.location, testmode=True)
        html_live = redcipe.get_content(self.url)
        self.assertIn("<!DOCTYPE html>", html_cached)
        self.assertIn("<!DOCTYPE html>", html_live)

    def test_make_soup_makes_soup(self):
        html_cached = redcipe.get_content(self.location, testmode=True)
        soup = redcipe.make_soup(html_cached)
        self.assertEqual("<class 'bs4.BeautifulSoup'>", str(type(soup)))

    def test_get_comments_finds_comments(self):
        html_cached = redcipe.get_content(self.location, testmode=True)
        soup = redcipe.make_soup(html_cached)
        comments = redcipe.get_comments(soup)
        self.assertNotEqual(len(comments), 0)

if __name__ == "__main__":
    unittest.main()