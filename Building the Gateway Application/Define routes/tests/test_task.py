import flask_unittest

from gateway.application import app


class TestClient(flask_unittest.ClientTestCase):
    # Assign the flask app object
    app = app

    def test_get_with_client(self, client):
        response = client.get('/items')
        self.assertEqual(response.data, b'Hello from GET')

    def test_get_id_with_client(self, client):
        response = client.get('/items/2')
        self.assertEqual(response.data, b'Hello from GET')

    def test_post_with_client(self, client):
        response = client.post('/items')
        self.assertEqual(response.data, b'Hello from POST')

    def test_delete_with_client(self, client):
        response = client.delete('/items/2')
        self.assertEqual(response.data, b'Hello from DELETE')

    def test_put_with_client(self, client):
        response = client.put('/items/2')
        self.assertEqual(response.data, b'Hello from PUT')
