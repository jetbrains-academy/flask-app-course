import flask_unittest

from api import app


class TestClient(flask_unittest.ClientTestCase):
    # Assign the flask app object
    app = app

    def test_get_with_client(self, client):
        response = client.get('/items')
        self.assertEqual(response.status_code, 200)

    def test_post_with_client(self, client):
        response = client.post('/items', json={"id": "100500", "name": "TestDevice", "location": "somewhere", "status": "off"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, (b'{"device": {"id": "100500", "name": "TestDevice", "location": "somewhere", "status": "off"}}\n'))

    def test_get__with_client(self, client):
        response = client.get('/items/001')
        self.assertEqual(response.data, b'{"device": {"id": "001", "name": "Light bulb", "location": "hall", "status": "off"}}\n')


    def test_put_with_client(self, client):
        response = client.put('/items/003', data={'location': 'hall', 'status': 'off'})
        self.assertEqual(response.status_code, 200)

    def test_delete_with_client(self, client):
        response = client.delete('/items/002')
        self.assertEqual(response.status_code, 201)