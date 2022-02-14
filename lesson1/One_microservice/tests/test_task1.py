import unittest
import requests
import random
import string


class TestCase(unittest.TestCase):
    def test_post(self):
        car_id = ''.join(random.choices(string.ascii_lowercase, k=10))
        test_car = {'name': f'TestCar_{car_id}'}
        response = requests.post('http://127.0.0.1:5000/books', json={'title': 'TestCar12345', 'author': 'Author', 'length': 234, 'rating': 0.9})
        print(response.text)
        self.assertEqual(response.status_code, 201, msg="Such a bad day :(")

    def test_add(self):
        response = requests.get('http://127.0.0.1:5000/books')
        # url = response.url
        # status_code = response.status_code
        print(response.url)
        print(response.status_code)
        print(response.text)
        self.assertEqual(response.status_code, 200, msg="Such a bad day :(")


