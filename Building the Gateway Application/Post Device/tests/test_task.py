import asyncio
import unittest
import requests
import docker
from common.test_with_docker_compose import TestWithDockerCompose

client = docker.from_env()


class TestTask(TestWithDockerCompose):
    healthcheck_url = 'http://127.0.0.1:5000/items'

    async def test_post(self):
        try:
            response = requests.post('http://127.0.0.1:5001/items', json={"id": "New_device_ID",
                                                                          "name": "UPDATE",
                                                                          "location": "location",
                                                                          "status": "off"})
            print(response.status_code)
            print(response.text)
            self.assertEqual(201, response.status_code, msg="POST request resulted in an unexpected response status code.")
            self.assertEqual((b'{\n  "Posted a device": {\n    "id": "New_device_ID",\n    "location": "location",'
                              b'\n    "name": "UPDATE",\n    "status": "off"\n  }\n}\n').decode("utf-8").replace(" ",
                                                                                                                 ""),
                             response.content.decode("utf-8").replace(" ", ""),
                             msg="POST request resulted in an unexpected response content.")
        except Exception as e:
            if isinstance(e, AssertionError):
                self.fail(msg=f"Unexpected response, {str(e)}")
            else:
                self.fail(msg=f'Something went wrong. Maybe your app is crashed: {str(e)}')
