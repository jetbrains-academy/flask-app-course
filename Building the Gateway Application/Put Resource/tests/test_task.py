import flask_unittest

from gateway.application import app


class TestClient(flask_unittest.ClientTestCase):
    # Assign the flask app object
    app = app

    def test_index(self, client):
        response = client.get('/')
        self.assertEqual(response.data, b'Hello from Gateway!')

    def test_get_with_client(self, client):
        response = client.get('/items')
        self.assertEqual(response.data, (b'{\n  "items": {\n    "001": {\n      "id": "001", \n      "location": "hall"'
                                         b', \n      "name": "Light bulb", \n      "status": "off"\n    }, \n    "002":'
                                         b' {\n      "id": "002", \n      "location": "bedroom", \n      "name": "Humi'
                                         b'dity_sensor", \n      "status": "on"\n    }\n  }\n}\n'))

    def test_get_id_with_client(self, client):
        response = client.get('/items/002')
        self.assertEqual(response.data, (b'{\n  "device": {\n    "id": "002", \n    "location": "bedroom", \n    "name"'
                                         b': "Humidity_sensor", \n    "status": "on"\n  }\n}\n'))

    def test_post_with_client(self, client):
        response = client.post('/items',
                               json={"id": "004", "name": "TestDevice", "location": "somewhere", "status": "off"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, (b'{\n  "device": {\n    "id": "004", \n    "location": "somewhere", \n    "nam'
                                         b'e": "TestDevice", \n    "status": "off"\n  }\n}\n'))

    def test_delete_with_client(self, client):
        response = client.delete('/items/003')
        self.assertEqual(response.status_code, 201)

    def test_put_with_client(self, client):
        response = client.put('/items/002', json={'location': 'hall', 'status': 'off'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, (b'{\n  "updated device": {\n    "id": "002", \n    "location": "hall", \n    "'
                                         b'name": "Humidity_sensor", \n    "status": "off"\n  }\n}\n'))
