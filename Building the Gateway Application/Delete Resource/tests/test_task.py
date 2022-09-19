# import flask_unittest
#
# from gateway.application import app
#
#
# class TestClient(flask_unittest.ClientTestCase):
#     # Assign the flask app object
#     app = app
#
#     def test_index(self, client):
#         response = client.get('/')
#         self.assertEqual(response.data, b'Hello from Gateway!')
#
#     def test_get_with_client(self, client):
#         response = client.get('/items')
#         self.assertEqual(response.data, (b'{\n  "items": {\n    "001": {\n      "id": "001", \n      "location": "hall"'
#                                          b', \n      "name": "Light bulb", \n      "status": "off"\n    }, \n    "002":'
#                                          b' {\n      "id": "002", \n      "location": "bedroom", \n      "name": "Humi'
#                                          b'dity_sensor", \n      "status": "on"\n    }, \n    "003": {\n      "id": "00'
#                                          b'3", \n      "location": "bedroom", \n      "name": "Humidifier", \n      "s'
#                                          b'tatus": "off"\n    }\n  }\n}\n'))
#
#     def test_get_id_with_client(self, client):
#         response = client.get('/items/002')
#         self.assertEqual(response.data, (b'{\n  "device": {\n    "id": "002", \n    "location": "bedroom", \n    "name"'
#                                          b': "Humidity_sensor", \n    "status": "on"\n  }\n}\n'))
#
#     # def test_post_with_client(self, client):
#     #     response = client.post('/items')
#     #     self.assertEqual(response.data, b'Hello from POST')
#     #
#     # def test_delete_with_client(self, client):
#     #     response = client.delete('/items/2')
#     #     self.assertEqual(response.data, b'Hello from DELETE')
#     #
#     # def test_put_with_client(self, client):
#     #     response = client.put('/items/2')
#     #     self.assertEqual(response.data, b'Hello from PUT')


import unittest
import requests
import random
import string
import time
from flask import jsonify

time.sleep(3)


class TestCase(unittest.TestCase):
    # def test_get(self):
    #     response = requests.get('http://127.0.0.1:5001/items')
    #     print(response.status_code)
    #     print(response.text)
    #     self.assertEqual(response.status_code, 200, msg=f"GET request resulted in an unexpected response code: {response.status_code}")
    #     self.assertEqual(response.content, (b'{\n  "items": {\n    "001": {\n      "id": "001", \n      "location": "hall"'
    #                                         b', \n      "name": "Light bulb", \n      "status": "off"\n    }, \n    "003":'
    #                                         b' {\n      "id": "003", \n      "location": "bedroom", \n      "name": "Humi'
    #                                         b'difier", \n      "status": "off"\n    }\n  }\n}\n'))
    #
    # def test_get_id(self):
    #     response = requests.get('http://127.0.0.1:5001/items/001')
    #     print(response.status_code)
    #     print(response.text)
    #     self.assertEqual(response.status_code, 200, msg=f"GET request resulted in an unexpected response code: {response.status_code}")
    #     self.assertEqual(response.content, (b'{\n  "device": {\n    "id": "001", \n    "location": "hall", \n    "name": "'
    #                                         b'Light bulb", \n    "status": "off"\n  }\n}\n'))

    def test_delete_404(self):
        response = requests.delete('http://127.0.0.1:5001/items/100')
        print(response.status_code)
        print(response.text)
        self.assertEqual(response.status_code, 404, msg=f"DELETE request resulted in an unexpected response code: {response.status_code}")
        self.assertEqual(response.content, b'{\n  "data": {}, \n  "message": "Device not found"\n}\n', msg="DELETE request resulted in unexpected response content.")

    def test_delete(self):
        response = requests.delete('http://127.0.0.1:5001/items/002')
        print(response.status_code)
        print(response.text)
        self.assertEqual(response.status_code, 201, msg=f"DELETE request resulted in an unexpected response code: {response.status_code}")
        self.assertEqual(response.content, b'{\n  "deleted device": "002"\n}\n', msg="DELETE request resulted in unexpected response content.")
