import flask_unittest

from api import app


class TestClient(flask_unittest.ClientTestCase):
    # Assign the flask app object
    app = app

    def test_get_with_client(self, client):
        response = client.get('/items')
        self.assertEqual(200, response.status_code, msg=f"GET request resulted in an unexpected response code {response.status_code}.")

    def test_post_with_client(self, client):
        response = client.post('/items', json={"id": "100500", "name": "TestDevice", "location": "somewhere", "status": "off"})
        self.assertEqual(201, response.status_code, msg=f"POST request resulted in an unexpected response code {response.status_code}.")
        self.assertEqual((b'{"device":{"id":"100500","location":"somewhere","name":"TestDevice","status"'
                                         b':"off"}}\n'), response.data, msg="POST request resulted in unexpected response content.")

    def test_get_id_with_client(self, client):
        response = client.get('/items/001')
        self.assertEqual(200, response.status_code, msg=f"GET request resulted in an unexpected response code {response.status_code}.")
        self.assertEqual((b'{"device":{"id":"001","location":"hall","name":"Light bulb","status":"off"}}'
                                         b'\n'), response.data, msg="GET request resulted in unexpected response content.")

    def test_put_with_client(self, client):
        response = client.put('/items/003', json={'location': 'hall', 'status': 'off'})
        self.assertEqual(200, response.status_code, msg=f"PUT request resulted in an unexpected response code {response.status_code}.")
        self.assertEqual((b'{"updated device":{"id":"003","location":"hall","name":"Humidifier","stat'
                                         b'us":"off"}}\n'), response.data, msg="PUT request resulted in unexpected response content.")

    def test_delete_with_client(self, client):
        response = client.delete('/items/002')
        self.assertEqual(201, response.status_code, msg=f"DELETE request resulted in an unexpected response code {response.status_code}.")
        self.assertEqual(b'{"deleted device":"002"}\n', response.data, msg="DELETE request resulted in unexpected response content.")

    def test_delete_with_client_error(self, client):
        response = client.delete('/items/002222')
        self.assertEqual(404, response.status_code, msg=f"DELETE request resulted in an unexpected response code {response.status_code}.")
        self.assertEqual(b'{"data":{},"message":"Device not found"}\n', response.data, msg="DELETE request resulted in unexpected response content.")

    def test_put_with_client_error(self, client):
        response = client.put('/items/003333', json={'location': 'hall', 'status': 'off'})
        self.assertEqual(404, response.status_code, msg=f"PUT request resulted in an unexpected response code {response.status_code}.")
        self.assertEqual(b'{"data":{},"message":"Device not found"}\n', response.data, msg="PUT request resulted in unexpected response content.")

    def test_get_with_client_error(self, client):
        response = client.get('/items/001111')
        self.assertEqual(404, response.status_code, msg=f"GET request resulted in an unexpected response code {response.status_code}.")
        self.assertEqual(b'{"data":{},"message":"Device not found"}\n', response.data, msg="GET request resulted in unexpected response content.")

    def test_post_with_client_error(self, client):
        response = client.post('/', json={"id": "100500", "name": "TestDevice", "location": "somewhere", "status": "off"})
        self.assertEqual(404, response.status_code, msg=f"POST request resulted in an unexpected response code {response.status_code}.")