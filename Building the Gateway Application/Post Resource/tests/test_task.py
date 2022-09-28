import unittest
import requests
import random
import string
import time

time.sleep(3)


class TestCase(unittest.TestCase):
    def test_post(self):
        # device_id = ''.join(random.choices(string.ascii_lowercase, k=10))
        response = requests.post('http://127.0.0.1:5001/items', json={"id": "New_device_ID",
                                                                      "name": "UPDATE",
                                                                      "location": "location",
                                                                      "status": "off"})
        print(response.status_code)
        print(response.text)
        self.assertEqual(201, response.status_code, msg="POST request resulted in an unexpected response status code.")
        self.assertEqual((b'{\n  "device": {\n    "id": "New_device_ID", \n    "location": "location", \n  '
                          b'  "name": "UPDATE", \n    "status": "off"\n  }\n}\n').decode("utf-8").replace(" ", ""),
                         response.content.decode("utf-8").replace(" ", ""),
                         msg="POST request resulted in an unexpected response content.")

