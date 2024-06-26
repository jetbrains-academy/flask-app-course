import flask_unittest

from api import app


class TestClient(flask_unittest.ClientTestCase):
    # Assign the flask app object
    app = app

    def test_put_with_client(self, client):
        response = client.put('/items/003', json={'location': 'hall', 'status': 'off'})
        self.assertEqual(200, response.status_code, msg=f"PUT request resulted in an unexpected response code {response.status_code}.")
        self.assertEqual(b'{"updated device":"003"}\n', response.data, msg="PUT request resulted in unexpected response content.")

    def test_get(self, client):
        response = client.get('/items')
        self.assertEqual(200, response.status_code, msg="The app does not seem to be responding properly")