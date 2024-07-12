import flask_unittest
import json

from api import app


class TestClient(flask_unittest.ClientTestCase):
    # Assign the flask app object
    app = app

    def test_get_with_client(self, client):
        response = client.get('/items')
        # Maybe we should reformat all such tests in this way =/
        actual_response = json.loads(response.data.decode('utf-8'))
        expected_response = {
            "items": {
                "001": {"id": "001", "location": "hall", "name": "Light bulb", "status": "off"},
                "002": {"id": "002", "location": "bedroom", "name": "Humidity sensor", "status": "on"},
                "003": {"id": "003", "location": "bedroom", "name": "Humidifier", "status": "off"}
            }
        }
        self.assertEqual(response.status_code, 200, msg=f"GET request resulted in an unexpected response code {response.status_code}.")
        self.assertEqual(actual_response, expected_response, msg="GET request resulted in unexpected response content.")

    def test_post_with_client(self, client):
        response = client.post('/items', json={"id": "100500", "name": "TestDevice", "location": "somewhere", "status": "off"})
        self.assertEqual(response.status_code, 201, msg=f"POST request resulted in an unexpected response code {response.status_code}.")
        self.assertEqual(response.data, (b'{"Posted a device":{"id":"100500","location":"somewhere","name":"TestDevice"'
                                         b',"status":"off"}}\n'), msg="POST request resulted in unexpected response content.")

    def test_post_err_id_with_client(self, client):
        response = client.post('/items', json={"name": "TestDevice", "location": "somewhere", "status": "off"})
        self.assertEqual(response.status_code, 400, msg="Argument 'id' must be required")

    def test_post_existing_id_with_client(self, client):
        response = client.post('/items', json={"id": "001", "name": "TestDevice", "location": "somewhere", "status": "off"})
        self.assertEqual(response.status_code, 400, msg=f"POST request resulted in an unexpected response code {response.status_code}.")


    def test_post_err_name_with_client(self, client):
        response = client.post('/items', json={"id": "100500", "location": "somewhere", "status": "off"})
        self.assertEqual(response.status_code, 400, msg="Argument 'name' must be required")

    def test_post_err_location_with_client(self, client):
        response = client.post('/items', json={"id": "100500", "name": "TestDevice", "status": "off"})
        self.assertEqual(response.status_code, 400, msg="Argument 'location' must be required")

    def test_post_err_status_with_client(self, client):
        response = client.post('/items', json={"id": "100500", "name": "TestDevice", "location": "somewhere"})
        self.assertEqual(response.status_code, 400, msg="Argument 'status' must be required")
