import flask_unittest

from .api_test import app


class TestClient(flask_unittest.ClientTestCase):
    # Assign the flask app object
    app = app

    def test_get_with_client(self, client):
        response = client.get('/items')
        self.assertEqual(response.status_code, 200)
        # This will fail on a second test attempt because the post method will add something
        # self.assertEqual(response.data, b'{"002": {"id": "002", "name": "Humidity_sensor", "location": "bedroom", '
        #                                 b'"status": "on"}, "001": {"id": "001", "name": "Light bulb", "location": '
        #                                 b'"hall", "status": "off"}, "003": {"id": "003", "name": "Humidifier", '
        #                                 b'"location": "bedroom", "status": "off"}}\n')
        assert b'"001": {"id": "001", "name": "Light bulb", "location": "hall", "status": "off"}' in response.data
