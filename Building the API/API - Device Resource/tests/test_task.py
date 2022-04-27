# import unittest
# import requests
#
#
# class TestCase(unittest.TestCase):
#     def test_get(self):
#         response = requests.get('http://0.0.0.0:5000/items/002')
#         print(response.status_code)
#         print(response.text)
#         self.assertEqual(response.status_code, 200, msg=f"GET request resulted in an unexpected response code: {response.status_code}")


import flask_unittest

from api import app


class TestClient(flask_unittest.ClientTestCase):
    # Assign the flask app object
    app = app

    def test_404_with_client(self, client):
        response = client.get('/items')
        self.assertEqual(response.status_code, 404)

    def test_get_with_client(self, client):
        response = client.get('/items/001')
        self.assertEqual(response.data, b'{"device": {"id": "001", "name": "Light bulb", "location": "hall", "status": "off"}}\n')

    def test_put_with_client(self, client):
        response = client.put('/items/003', data={'location': 'hall', 'status': 'off'})
        self.assertEqual(response.status_code, 200)

    def test_delete_with_client(self, client):
        response = client.delete('/items/002')
        self.assertEqual(response.status_code, 200)