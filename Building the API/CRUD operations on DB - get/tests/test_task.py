import flask_unittest
from api import app


class TestClient(flask_unittest.ClientTestCase):
    # Assign the flask app object
    app = app

    def test_get_with_client_01(self, client):
        response = client.get('/items')
        self.assertEqual(200, response.status_code, msg=f"GET request resulted in an unexpected response code {response.status_code}.")

    def test_get_with_client_02(self, client):
        response = client.get('/items')
        self.assertEqual(response.data, (b'{"items":{"001":{"id":"001","location":"hall","name":"Light bulb","status":"'
                          b'off"},"002":{"id":"002","location":"bedroom","name":"Humidity_sensor","statu'
                          b's":"on"},"003":{"id":"003","location":"bedroom","name":"Humidifier","status"'
                          b':"off"}}}\n'), msg="GET request resulted in unexpected response content. You should get the data from dal, not from the dictionary.")
