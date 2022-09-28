import unittest
import requests
import time

time.sleep(3)


class TestCase(unittest.TestCase):
    def test_get(self):
        response = requests.get('http://127.0.0.1:5001/items')
        print(response.status_code)
        print(response.text)
        self.assertEqual(200, response.status_code,
                         msg=f"GET request resulted in an unexpected response code: {response.status_code}")
        self.assertEqual((b'{\n  "items": {\n    "001": {\n      "id": "001",\n      "location": "hall",'
                          b'\n      "name": "Light bulb",\n      "status": "off"\n    },\n    "002":'
                          b' {\n      "id": "002",\n      "location": "bedroom",\n      "name": "Humidi'
                          b'ty_sensor",\n      "status": "on"\n    },\n    "003": {\n      "id": "00'
                          b'3",\n      "location": "bedroom",\n      "name": "Humidifier",\n      "stat'
                          b'us": "off"\n    }\n  }\n}\n').decode("utf-8").replace(" ", ""),
                         response.content.decode("utf-8").replace(" ", ""),
                         msg="GET request resulted in unexpected response content.")

    def test_get_id(self):
        response = requests.get('http://127.0.0.1:5001/items/001')
        print(response.status_code)
        print(response.text)
        self.assertEqual(200, response.status_code,
                         msg=f"GET request resulted in an unexpected response code: {response.status_code}")
        self.assertEqual((b'{\n  "device": {\n    "id": "001", \n    "location": "hall", \n    "name": "'
                          b'Light bulb", \n    "status": "off"\n  }\n}\n').decode("utf-8").replace(" ", ""),
                         response.content.decode("utf-8").replace(" ", ""),
                         msg="GET request resulted in unexpected response content.")

    def test_get_id_err(self):
        response = requests.get('http://127.0.0.1:5001/items/00111')
        print(response.status_code)
        print(response.text)
        self.assertEqual(404, response.status_code,
                         msg=f"GET request resulted in an unexpected response code: {response.status_code}")
        self.assertEqual(b'{\n  "data": {}, \n  "message": "Device not found"\n}\n'.decode("utf-8").replace(" ", ""),
                         response.content.decode("utf-8").replace(" ", ""),
                         msg="GET request resulted in unexpected response content.")
