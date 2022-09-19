import flask_unittest

from api import app


class TestClient(flask_unittest.ClientTestCase):
    # Assign the flask app object
    app = app

    def test_get_with_client(self, client):
        response = client.get('/items')
        self.assertEqual(response.status_code, 200, msg=f"GET request resulted in an unexpected response code {response.status_code}.")
        self.assertEqual(response.data, (b'{"items":{"001":{"id":"001","location":"hall","name":"Light bulb","status":"'
                                         b'off"},"002":{"id":"002","location":"bedroom","name":"Humidity_sensor","statu'
                                         b's":"on"},"003":{"id":"003","location":"bedroom","name":"Humidifier","status"'
                                         b':"off"}}}\n'), msg="GET request resulted in unexpected response content.")

    def test_post_with_client(self, client):
        response = client.post('/items', json={"id": "100500", "name": "TestDevice", "location": "somewhere", "status": "off"})
        self.assertEqual(response.status_code, 201, msg=f"POST request resulted in an unexpected response code {response.status_code}.")
        self.assertEqual(response.data, (b'{"Posted a device":{"id":"100500","location":"somewhere","name":"TestDevice"'
                                         b',"status":"off"}}\n'), msg="POST request resulted in unexpected response content.")

    def test_post_err_id_with_client(self, client):
        response = client.post('/items', json={"name": "TestDevice", "location": "somewhere", "status": "off"})
        self.assertEqual(response.status_code, 400, msg="Argument 'id' must be required")

    def test_post_err_name_with_client(self, client):
        response = client.post('/items', json={"id": "100500", "location": "somewhere", "status": "off"})
        self.assertEqual(response.status_code, 400, msg="Argument 'name' must be required")

    def test_post_err_location_with_client(self, client):
        response = client.post('/items', json={"id": "100500", "name": "TestDevice", "status": "off"})
        self.assertEqual(response.status_code, 400, msg="Argument 'location' must be required")

    def test_post_err_status_with_client(self, client):
        response = client.post('/items', json={"id": "100500", "name": "TestDevice", "location": "somewhere"})
        self.assertEqual(response.status_code, 400, msg="Argument 'status' must be required")



    # def test_get_id_with_client(self, client):
    #     response = client.get('/items/001')
    #     self.assertEqual(response.data, b'{"device": {"id": "001", "name": "Light bulb", "location": "hall", "status": "off"}}\n')
    #
    #
    # def test_put_with_client(self, client):
    #     response = client.put('/items/003', data={'location': 'hall', 'status': 'off'})
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_delete_with_client(self, client):
    #     response = client.delete('/items/002')
    #     self.assertEqual(response.status_code, 201)