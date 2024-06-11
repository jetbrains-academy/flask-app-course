import flask_unittest

from api import app


class TestClient(flask_unittest.ClientTestCase):
    # Assign the flask app object
    app = app

    def test_get_id_with_client(self, client):
        response = client.get('/items/001')
        self.assertEqual(response.status_code, 200, msg=f"GET request resulted in an unexpected response code {response.status_code}.")
        self.assertEqual(b'{"id":"001","location":"hall","name":"Light bulb","status":"off"}\n', response.data, msg="GET request resulted in unexpected response content.")


    def test_get_id_with_client_404(self, client):
        response = client.get('/items/00111111')
        self.assertEqual(response.status_code, 404, msg=f"GET request resulted in an unexpected response code {response.status_code}. When trying to get an non-existent item a response code 400 should be returned.")
        # Not sure if we should be checking this (we could)
        # self.assertEqual(b'{"message":"Device not found"}\n', response.data, msg="GET request resulted in unexpected response content.")

