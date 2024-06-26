import asyncio
import unittest
import requests
import docker
from common.test_with_docker_compose import TestWithDockerCompose

client = docker.from_env()


class TestTask(TestWithDockerCompose):
    healthcheck_url = 'http://127.0.0.1:5000/items'

    async def test_put(self):
        try:
            response = requests.put('http://127.0.0.1:5001/items/002', json={"id": "002",
                                                                                 "name": "Humidity_sensor",
                                                                                 "location": "bedroom",
                                                                                 "status": "off"})
            print(response.status_code)
            print(response.text)
            self.assertEqual(200, response.status_code,
                             msg=f"PUT request resulted in an unexpected response code: {response.status_code}")
            self.assertEqual((b'{\n  "updated device": "002"\n}\n').decode("utf-8").replace(" ", ""),
                             response.content.decode("utf-8").replace(" ", ""),
                             msg="PUT request resulted in an unexpected response content.")
        except Exception as e:
            if type(e) == AssertionError:
                self.fail(msg=f"Unexpected response, {str(e)}")
            else:
                self.fail(msg=f'Something went wrong. Maybe your app is crashed: {str(e)}')

    async def test_put_err(self):
        try:
            response = requests.put('http://127.0.0.1:5001/items/002222', json={"id": "002222",
                                                                                "name": "Humidity_sensor",
                                                                                "location": "bedroom",
                                                                                "status": "off"})
            print(response.status_code)
            print(response.text)
            self.assertEqual(404, response.status_code,
                             msg=f"PUT request resulted in an unexpected response code: {response.status_code}")
            self.assertEqual(b'{\n  "message": "Device not found"\n}\n'.decode("utf-8").replace(" ", ""),
                             response.content.decode("utf-8").replace(" ", ""),
                             msg="PUT request resulted in unexpected response content.")
        except Exception as e:
            if isinstance(e, AssertionError):
                self.fail(msg=f"Unexpected response, {str(e)}")
            else:
                self.fail(msg=f'Something went wrong. Maybe your app is crashed: {str(e)}')
