import flask_unittest

from .api_test import app


class TestClient(flask_unittest.ClientTestCase):
    # Assign the flask app object
    app = app

    def test_get_with_client(self, client):
        response = client.get('/items')
        self.assertEqual(response.status_code, 200, msg=f"GET request resulted in an unexpected response code {response.status_code}.")
        self.assertEqual(response.data, (b'{"004": {"id": "004", "name": "TestDevice", "location": "somewhere", "status'
                                         b'": "off"}, "002": {"id": "002", "name": "Humidity_sensor", "location": "bedr'
                                         b'oom", "status": "on"}, "001": {"id": "001", "name": "Light bulb", "location"'
                                         b': "hall", "status": "off"}, "003": {"id": "003", "name": "Humidifier", "loca'
                                         b'tion": "bedroom", "status": "off"}}\n'), msg="GET request resulted in unexpected response content.")
