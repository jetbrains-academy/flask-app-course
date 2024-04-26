import flask_unittest

from api import app


class TestClient(flask_unittest.ClientTestCase):
    # Assign the flask app object
    app = app

    def test_delete_with_client(self, client):
        response = client.delete('/items/002')
        self.assertEqual(response.status_code, 200, msg=f"DELETE request resulted in an unexpected response code {response.status_code}.")
        self.assertEqual(response.data, b'{"message":"Device deleted"}\n', msg="DELETE request resulted in unexpected response content.")
