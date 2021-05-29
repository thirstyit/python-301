import unittest
import rescrape


class TestRescrape(unittest.TestCase):
    # requests can establish a connection and receive a valid response
    def test_get_valid_html_response(self):
        BASE_URL = "https://codingnomads.github.io/recipes/"
        index_page = rescrape.get_page_content(BASE_URL)
        self.assertEqual(index_page.status_code, 200)
    
if __name__ == "__main__":
    unittest.main()