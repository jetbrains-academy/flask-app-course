import unittest
import requests
import random
import string
import time

time.sleep(3)


class TestCase(unittest.TestCase):
    def test_put(self):
        response = requests.put('http://127.0.0.1:5001/items/002', json={"id": "002",
                                                                         "name": "Humidity_sensor",
                                                                         "location": "bedroom",
                                                                         "status": "off"})
        print(response.status_code)
        print(response.text)
        self.assertEqual(200, response.status_code,
                         msg=f"PUT request resulted in an unexpected response code: {response.status_code}")
        self.assertEqual((b'{\n  "updated device": {\n    "id": "002", \n    "location": "bedroom", \n  '
                          b'  "name": "Humidity_sensor", \n    "status": "off"\n  }\n}\n').decode("utf-8").replace(" ", ""),
                         response.content.decode("utf-8").replace(" ", ""),
                         msg="PUT request resulted in an unexpected response content.")

    def test_put_err(self):
        response = requests.put('http://127.0.0.1:5001/items/002222', json={"id": "002222",
                                                                            "name": "Humidity_sensor",
                                                                            "location": "bedroom",
                                                                            "status": "off"})
        print(response.status_code)
        print(response.text)
        self.assertEqual(404, response.status_code,
                         msg=f"PUT request resulted in an unexpected response code: {response.status_code}")
        self.assertEqual(b'{\n  "data": {}, \n  "message": "Device not found"\n}\n'.decode("utf-8").replace(" ", ""),
                         response.content.decode("utf-8").replace(" ", ""),
                         msg="PUT request resulted in unexpected response content.")
