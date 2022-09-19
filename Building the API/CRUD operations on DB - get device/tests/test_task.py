import flask_unittest

from .api_test import app


class TestClient(flask_unittest.ClientTestCase):
    # Assign the flask app object
    app = app

    def test_get_id_with_client(self, client):
        response = client.get('/items/001')
        self.assertEqual(response.status_code, 200, msg=f"GET request resulted in an unexpected response code {response.status_code}.")
        self.assertEqual(response.data, b'{"device": {"id": "001", "name": "Light bulb", "location": "hall", '
                                        b'"status": "off"}}\n', msg="GET request resulted in unexpected response content.")

