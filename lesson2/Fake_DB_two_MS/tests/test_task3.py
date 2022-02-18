import unittest
import requests
import random
import string
import time

time.sleep(3)

class TestCase(unittest.TestCase):
    def test_post(self):
        book_id = ''.join(random.choices(string.ascii_lowercase, k=10))
        response = requests.post('http://127.0.0.1:5001/books', json={'title': f'TestBook_{book_id}', 'author': 'Author', 'length': 234, 'rating': 0.9})
        print(response.status_code)
        print(response.text)
        self.assertEqual(response.status_code, 201, msg="Such a bad day :(")

    def test_get(self):
        response = requests.get('http://127.0.0.1:5001/books')
        print(response.status_code)
        print(response.text)
        self.assertEqual(response.status_code, 200, msg=f"GET request resulted in an unexpected response code: {response.status_code}")

    def test_put(self):
        book_id = ''.join(random.choices(string.ascii_lowercase, k=10))
        response = requests.put('http://127.0.0.1:5001/books/2', json={'title': f'TestBook_{book_id}', 'author': 'Author', 'length': 100, 'rating': 5.0})
        print(response.status_code)
        print(response.text)
        self.assertEqual(response.status_code, 200, msg=f"PUT request resulted in an unexpected response code: {response.status_code}")

    def test_delete(self):
        response = requests.delete('http://127.0.0.1:5001/books/100')
        print(response.status_code)
        print(response.text)
        self.assertEqual(response.status_code, 404, msg=f"DELETE request resulted in an unexpected response code: {response.status_code}")
