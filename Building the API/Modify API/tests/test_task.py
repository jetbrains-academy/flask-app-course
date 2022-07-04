import flask_unittest

from api import app


class TestClient(flask_unittest.ClientTestCase):
    # Assign the flask app object
    app = app

    def test_get_with_client(self, client):
        response = client.get('/items')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, (b'{"items":{"001":{"id":"001","location":"hall","name":"Light bulb","status":"'
                                         b'off"},"003":{"id":"003","location":"bedroom","name":"Humidifier","status":"o'
                                         b'ff"},"100500":{"id":"100500","location":"somewhere","name":"TestDevice","sta'
                                         b'tus":"off"}}}\n'))

    def test_post_with_client(self, client):
        response = client.post('/items', json={"id": "100500", "name": "TestDevice", "location": "somewhere", "status": "off"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, (b'{"device":{"id":"100500","location":"somewhere","name":"TestDevice","status"'
                                         b':"off"}}\n'))

    def test_get__with_client(self, client):
        response = client.get('/items/001')
        self.assertEqual(response.data, (b'{"device":{"id":"001","location":"hall","name":"Light bulb","status":"off"}}'
                                         b'\n'))

    def test_put_with_client(self, client):
        response = client.put('/items/003', data={'location': 'hall', 'status': 'off'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, (b'{"updated device":{"id":"003","location":"bedroom","name":"Humidifier","stat'
                                         b'us":"off"}}\n'))

    def test_delete_with_client(self, client):
        response = client.delete('/items/002')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, b'{"deleted device":"002"}\n')

    def test_delete_with_client_error(self, client):
        response = client.delete('/items/002222')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data, b'{"data":{},"message":"Device not found"}\n')

    def test_put_with_client_error(self, client):
        response = client.put('/items/003333', data={'location': 'hall', 'status': 'off'})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data, b'{"data":{},"message":"Device not found"}\n')

    def test_get_with_client_error(self, client):
        response = client.get('/items/001111')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data, b'{"data":{},"message":"Device not found"}\n')

    def test_post_with_client_error(self, client):
        response = client.post('/', json={"id": "100500", "name": "TestDevice", "location": "somewhere", "status": "off"})
        self.assertEqual(response.status_code, 404)