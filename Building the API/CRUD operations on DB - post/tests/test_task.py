import flask_unittest

from .api_test import app


class TestClient(flask_unittest.ClientTestCase):
    # Assign the flask app object
    app = app

    def test_post_with_client(self, client):
        response = client.post('/items',
                               json={"id": "004", "name": "TestDevice", "location": "somewhere", "status": "off"})
        self.assertEqual(response.status_code, 201, msg=f"POST request resulted in an unexpected response code {response.status_code}.")
        self.assertEqual(response.data, (b'{"device": {"id": "004", "name": "TestDevice", "location": "somewhere", "sta'
                                         b'tus": "off"}}\n'), msg="POST request resulted in unexpected response content.")

