import unittest
import requests
import random
import string
import time

time.sleep(3)

class TestCase(unittest.TestCase):
    def test_post(self):
        device_id = ''.join(random.choices(string.ascii_lowercase, k=10))
        response = requests.post('http://0.0.0.0:5000/items', json={"id": f"{device_id}",
                                                                      "name": "UPDATEDUPDATEDUPDATED",
                                                                      "location": "location",
                                                                      "status": "off"})
        print(response.status_code)
        print(response.text)
        self.assertEqual(201, response.status_code, msg="Such a bad day :(")

    def test_get(self):
        response = requests.get('http://0.0.0.0:5000/items')
        print(response.status_code)
        print(response.text)
        self.assertEqual(200, response.status_code, msg=f"GET request resulted in an unexpected response code: {response.status_code}")

    def test_put(self):
        # device_id = ''.join(random.choices(string.ascii_lowercase, k=10))
        response = requests.put('http://0.0.0.0:5000/items/002', json={"id": "002",
                                                                         "name": "Humidity_sensor",
                                                                         "location": "bedroom",
                                                                         "status": "off"})
        print(response.status_code)
        print(response.text)
        self.assertEqual(200, response.status_code, msg=f"PUT request resulted in an unexpected response code: {response.status_code}")

    def test_delete(self):
        response = requests.delete('http://0.0.0.0:5000/items/100')
        print(response.status_code)
        print(response.text)
        self.assertEqual(404, response.status_code, msg=f"DELETE request resulted in an unexpected response code: {response.status_code}")
