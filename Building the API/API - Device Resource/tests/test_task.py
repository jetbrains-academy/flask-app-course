import unittest
import requests
from api import Device


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_get(self):
        response = requests.get('http://0.0.0.0:5000/items/002')
        print(response.status_code)
        print(response.text)
        self.assertEqual(response.status_code, 200, msg=f"GET request resulted in an unexpected response code: {response.status_code}")
