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
#                                          b'dity_sensor", \n      "status": "on"\n    }\n  }\n}\n'))

    # def test_get_id_with_client(self, client):
    #     response = client.get('/items/002')
    #     self.assertEqual(response.data, (b'{\n  "device": {\n    "id": "002", \n    "location": "bedroom", \n    "name"'
    #                                      b': "Humidity_sensor", \n    "status": "on"\n  }\n}\n'))
    #
    # def test_post_with_client(self, client):
    #     response = client.post('/items',
    #                            json={"id": "004", "name": "TestDevice", "location": "somewhere", "status": "off"})
    #     self.assertEqual(response.status_code, 201)
    #     self.assertEqual(response.data, (b'{\n  "device": {\n    "id": "004", \n    "location": "somewhere", \n    "nam'
    #                                      b'e": "TestDevice", \n    "status": "off"\n  }\n}\n'))
    #
    # def test_delete_with_client(self, client):
    #     response = client.delete('/items/003')
    #     self.assertEqual(response.status_code, 201)
    #
    # def test_put_with_client(self, client):
    #     response = client.put('/items/002', json={'location': 'hall', 'status': 'off'})
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.data, (b'{\n  "updated device": {\n    "id": "002", \n    "location": "hall", \n    "'
    #                                      b'name": "Humidity_sensor", \n    "status": "off"\n  }\n}\n'))


import unittest
import requests
import random
import string
import time

time.sleep(3)

class TestCase(unittest.TestCase):
    # def test_post(self):
    #     device_id = ''.join(random.choices(string.ascii_lowercase, k=10))
    #     response = requests.post('http://127.0.0.1:5001/items', json={"id": f"{device_id}",
    #                                                                   "name": "UPDATEDUPDATEDUPDATED",
    #                                                                   "location": "location",
    #                                                                   "status": "off"})
    #     print(response.status_code)
    #     print(response.text)
    #     self.assertEqual(response.status_code, 201, msg="Such a bad day :(")
    #
    # def test_get(self):
    #     response = requests.get('http://127.0.0.1:5001/items')
    #     print(response.status_code)
    #     print(response.text)
    #     self.assertEqual(response.status_code, 200, msg=f"GET request resulted in an unexpected response code: {response.status_code}")

    def test_put(self):
        response = requests.put('http://127.0.0.1:5001/items/002', json={"id": "002",
                                                                         "name": "Humidity_sensor",
                                                                         "location": "bedroom",
                                                                         "status": "off"})
        print(response.status_code)
        print(response.text)
        self.assertEqual(response.status_code, 200, msg=f"PUT request resulted in an unexpected response code: {response.status_code}")
        self.assertEqual(response.content, (b'{\n  "updated device": {\n    "id": "002", \n    "location": "bedroom", \n  '
                                            b'  "name": "Humidity_sensor", \n    "status": "off"\n  }\n}\n'), msg="PUT request resulted in an unexpected response content.")

    def test_put_err(self):
        response = requests.put('http://127.0.0.1:5001/items/002222', json={"id": "002222",
                                                                         "name": "Humidity_sensor",
                                                                         "location": "bedroom",
                                                                         "status": "off"})
        print(response.status_code)
        print(response.text)
        self.assertEqual(response.status_code, 404, msg=f"PUT request resulted in an unexpected response code: {response.status_code}")
        self.assertEqual(response.content, b'{\n  "data": {}, \n  "message": "Device not found"\n}\n', msg="PUT request resulted in unexpected response content.")
    # def test_delete(self):
    #     response = requests.delete('http://127.0.0.1:5001/items/100')
    #     print(response.status_code)
    #     print(response.text)
    #     self.assertEqual(response.status_code, 404, msg=f"DELETE request resulted in an unexpected response code: {response.status_code}")
