import flask_unittest

from .api_test import app


class TestClient(flask_unittest.ClientTestCase):
    # Assign the flask app object
    app = app

    def test_put_with_client(self, client):
        response = client.put('/items/003', data={'location': 'hall', 'status': 'off'})
        self.assertEqual(response.status_code, 200, msg=f"PUT request resulted in an unexpected response code {response.status_code}.")
        self.assertEqual(response.data, (b'{"updated device": {"id": "003", "name": "Humidifier", "location": "bedroom"'
                                         b', "status": "off"}}\n'), msg="PUT request resulted in unexpected response content.")

