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
        self.assertEqual(response.status_code, 200, msg=f"GET request resulted in an unexpected response code {response.status_code}.")
        self.assertEqual(response.data,
                         b'{"id":"001","location":"hall","name":"Light bulb","status":"off"}\n',
                         msg="GET request resulted in unexpected response content.")

    def test_put_with_client(self, client):
        response = client.put('/items/003', json={'location': 'hall', 'status': 'off'})
        self.assertEqual(response.status_code, 200, msg=f"PUT request resulted in an unexpected response code {response.status_code}.")
        self.assertEqual(response.data, b'{"updated device":"003"}\n',
                         msg="PUT request resulted in unexpected response content.")

    def test_delete_with_client(self, client):
        response = client.delete('/items/002')
        self.assertEqual(response.status_code, 200, msg=f"DELETE request resulted in an unexpected response code {response.status_code}.")
        self.assertEqual(response.data, b'{"message":"Device deleted"}\n',
                         msg="DELETE request resulted in unexpected response content.")
