
import unittest
import requests
import random
import string
import time
from flask import jsonify

time.sleep(3)


class TestCase(unittest.TestCase):

    def test_delete_404(self):
        response = requests.delete('http://127.0.0.1:5001/items/100')
        print(response.status_code)
        print(response.text)
        self.assertEqual(404, response.status_code, msg=f"DELETE request resulted in an unexpected response code: {response.status_code}")
        self.assertEqual(b'{\n  "data": {}, \n  "message": "Device not found"\n}\n'.decode("utf-8").replace(" ", ""),
                         response.content.decode("utf-8").replace(" ", ""),
                         msg="DELETE request resulted in unexpected response content.")

    def test_delete(self):
        response = requests.delete('http://127.0.0.1:5001/items/002')
        print(response.status_code)
        print(response.text)
        self.assertEqual(201, response.status_code,
                         msg=f"DELETE request resulted in an unexpected response code: {response.status_code}")
        self.assertEqual(b'{\n  "deleted device": "002"\n}\n'.decode("utf-8").replace(" ", ""),
                         response.content.decode("utf-8").replace(" ", ""),
                         msg="DELETE request resulted in unexpected response content.")
