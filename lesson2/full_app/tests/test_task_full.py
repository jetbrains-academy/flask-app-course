import unittest
import requests
import random
import string
import time

time.sleep(3)

class TestCase(unittest.TestCase):
    def test_post(self):
        device_id = ''.join(random.choices(string.ascii_lowercase, k=10))
        response = requests.post('http://127.0.0.1:5001/items', json={"id": f"{device_id}",
                                                                      "name": "UPDATEDUPDATEDUPDATED",
                                                                      "device_type": "UPDATEDUPDATEDUPDATED",
                                                                      "controller_gateway": 1111})
        print(response.status_code)
        print(response.text)
        self.assertEqual(response.status_code, 201, msg="Such a bad day :(")

    def test_get(self):
        response = requests.get('http://127.0.0.1:5001/items')
        print(response.status_code)
        print(response.text)
        self.assertEqual(response.status_code, 200, msg=f"GET request resulted in an unexpected response code: {response.status_code}")

    def test_put(self):
        device_id = ''.join(random.choices(string.ascii_lowercase, k=10))
        response = requests.put('http://127.0.0.1:5001/items/002def', json={"id": f"{device_id}",
                                                                            "name": f"Updated_name",
                                                                            "device_type": "sensor",
                                                                            "controller_gateway": 1111})
        print(response.status_code)
        print(response.text)
        self.assertEqual(response.status_code, 200, msg=f"PUT request resulted in an unexpected response code: {response.status_code}")

    def test_delete(self):
        response = requests.delete('http://127.0.0.1:5001/items/100')
        print(response.status_code)
        print(response.text)
        self.assertEqual(response.status_code, 404, msg=f"DELETE request resulted in an unexpected response code: {response.status_code}")
