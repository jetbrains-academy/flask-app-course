import flask_unittest

from api import app


class TestClient(flask_unittest.ClientTestCase):
    # Assign the flask app object
    app = app

    def test_post_with_client(self, client):
        response = client.post('/items',
                               json={"id": "00444", "name": "TestDevice", "location": "somewhere", "status": "off"})
        self.assertEqual(response.status_code, 201, msg=f"POST request resulted in an unexpected response code {response.status_code}.")
        self.assertEqual(response.data, (b'{"Posted a device":{"id":"00444","location":"somewhere","name":"TestDevice","'
                                         b'status":"off"}}\n'), msg="POST request resulted in unexpected response content.")

    def test_post_with_client_400(self, client):
        response = client.post('/items',
                               json={"id": "00111", "name": "TestDevice", "location": "somewhere"})
        self.assertEqual(response.status_code, 400, msg=f"POST request resulted in an unexpected response code {response.status_code}. Make sure you validate device schema to avoid posting incomplete entries.")
        # Not sure if we should be checking the exact message here
        # self.assertEqual(response.data, (b'["ValidationError: ",{"status":["Missing data for required field."]}]\n'), msg="POST request resulted in unexpected response content.")


    def test_post_with_client_400_existing_item(self, client):
        response = client.post('/items',
                               json={"id": "001", "name": "TestDevice", "location": "somewhere", "status": "off"})
        self.assertEqual(response.status_code, 400, msg=f"POST request resulted in an unexpected response code {response.status_code}. Already existing item cannot be posted again.")
        # Not sure if we should be checking the exact message here
        # self.assertEqual(response.data, (b'{"message":"Device with this ID already exists."}\n'), msg="POST request resulted in unexpected response content.")

