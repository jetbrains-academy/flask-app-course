import unittest
import requests
import random
import string


class TestCase(unittest.TestCase):
    def test_get_3(self):
        response = requests.get('http://0.0.0.0:5001/api/cars')
        print(response.url)
        print(response.status_code)
        self.assertEqual(200, response.status_code, msg="Such a bad day :(")

    def test_post_3(self):
        car_id = ''.join(random.choices(string.ascii_lowercase, k=10))
        response = requests.post('http://0.0.0.0:5001/api/cars', json={'name': f'TestCar_{car_id}'})
        print(response.text)
        self.assertEqual(201, response.status_code, msg="Such a bad day :(")


