import asyncio
import unittest
import requests
import docker
import subprocess
import time
from common.test_with_docker_compose import TestWithDockerCompose

client = docker.from_env()


class TestTask(TestWithDockerCompose):
    healthcheck_url = 'http://127.0.0.1:5000/items'

    async def test_get(self):
        try:
            response = requests.get('http://127.0.0.1:5001/items')
            print(response.status_code)
            print(response.text)
            self.assertEqual(200, response.status_code,
                             msg=f"GET request resulted in an unexpected response code: {response.status_code}")
            self.assertEqual((b'{\n  "items": {\n    "001": {\n      "id": "001",\n      "location": "hall",'
                              b'\n      "name": "Light bulb",\n      "status": "off"\n    },\n    "002":'
                              b' {\n      "id": "002",\n      "location": "bedroom",\n      "name": "Humidi'
                              b'ty_sensor",\n      "status": "on"\n    },\n    "003": {\n      "id": "00'
                              b'3",\n      "location": "bedroom",\n      "name": "Humidifier",\n      "stat'
                              b'us": "off"\n    }\n  }\n}\n').decode("utf-8").replace(" ", ""),
                             response.content.decode("utf-8").replace(" ", ""),
                             msg="GET request resulted in unexpected response content.")
        except Exception as e:
            if type(e) == AssertionError:
                self.fail(msg=f"Unexpected response for GET /items, {str(e)}")
            else:
                self.fail(msg=f'Something went wrong. Maybe your app is crashed: {str(e)}')

    async def test_get_id(self):
        try:
            response = requests.get('http://127.0.0.1:5001/items/001')
            print(response.status_code)
            print(response.text)
            self.assertEqual(200, response.status_code,
                             msg=f"GET request resulted in an unexpected response code: {response.status_code}")
            self.assertEqual(b'{\n  "id": "001",\n  "location": "hall",\n  "name": "Light bulb",\n  "status": '
                             b'"off"\n}\n'.decode("utf-8").replace(" ", ""),
                             response.content.decode("utf-8").replace(" ", ""),
                             msg="GET request resulted in unexpected response content.")
        except Exception as e:
            if isinstance(e, AssertionError):
                self.fail(msg=f"Unexpected response for GET /items/001, {str(e)}")
            else:
                self.fail(msg=f'Something went wrong. Maybe your app is crashed: {str(e)}')

    async def test_get_id_err(self):
        try:
            response = requests.get('http://127.0.0.1:5001/items/00111')
            print(response.status_code)
            print(response.text)
            self.assertEqual(404, response.status_code,
                             msg=f"GET request resulted in an unexpected response code: {response.status_code}")
            self.assertEqual(b'{\n  "message": "Device not found"\n}\n'.decode("utf-8").replace(" ", ""),
                             response.content.decode("utf-8").replace(" ", ""),
                             msg="GET request resulted in unexpected response content.")
        except Exception as e:
            if isinstance(e, AssertionError):
                self.fail(msg=f"Unexpected response fir GET /items/00111, {str(e)}")
            else:
                self.fail(msg=f'Something went wrong. Maybe your app is crashed: {str(e)}')
