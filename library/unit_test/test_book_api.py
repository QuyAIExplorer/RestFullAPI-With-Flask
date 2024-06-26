import unittest
import requests

URL_GET_BOOK_BY_ID = "http://127.0.0.1:5000/book-management/book"
URL_GET_ALL_BOOK = "http://127.0.0.1:5000/book-management/books"

class TestBookApi(unittest.TestCase):
    # Positive testcase ( pass correct and expect correct)
    def test_get_all_book(self):
        response = requests.get(URL_GET_ALL_BOOK)
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.json()) , 0)

    def test_get_book_by_id(self):
        response = requests.get(URL_GET_BOOK_BY_ID + "/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["page_count"] , 200)
    
    # Negative testcase (pass incorrect and expect incorrect)
    def test_get_book_by_id_negative(self):
        response = requests.get(URL_GET_BOOK_BY_ID + "/3000")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(len(response.json()),1)