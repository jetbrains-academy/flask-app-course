import asyncio
import unittest
import requests
import docker
from common.test_with_docker_compose import TestWithDockerCompose

client = docker.from_env()


class TestTask(TestWithDockerCompose):
    healthcheck_url = 'http://127.0.0.1:5000/items'

    async def test_delete_404(self):
        try:
            response = requests.delete('http://127.0.0.1:5001/items/100')

            print(response.status_code)
            # TODO this turns out really bad in case of 500 response - several screens of bs html in the console
            print(response.text)
            self.assertEqual(404, response.status_code,
                             msg=f"DELETE request resulted in an unexpected response code: {response.status_code}")
            self.assertEqual(b'{\n  "message": "Device not found"\n}\n'.decode("utf-8").replace(" ", ""),
                             response.content.decode("utf-8").replace(" ", ""),
                             msg="DELETE request resulted in unexpected response content.")
        except Exception as e:
            if isinstance(e, AssertionError):
                self.fail(msg=f"Unexpected response for DELETE /items/100, {str(e)}")
            else:
                self.fail(msg=f'Something went wrong. Maybe your app is crashed: {str(e)}')

    async def test_delete(self):
        try:
            response = requests.delete('http://127.0.0.1:5001/items/002')

            print(response.status_code)
            # TODO this turns out really bad in case of 500 response - several screens of bs html in the console
            print(response.text)
            self.assertEqual(200, response.status_code,
                             msg=f"DELETE request resulted in an unexpected response code: {response.status_code}")
            self.assertEqual(b'{\n  "message": "Device deleted"\n}\n'.decode("utf-8").replace(" ", ""),
                             response.content.decode("utf-8").replace(" ", ""),
                             msg="DELETE request resulted in unexpected response content.")
        except Exception as e:
            if isinstance(e, AssertionError):
                self.fail(msg=f"Unexpected response for DELETE /items/002, {str(e)}")
            else:
                self.fail(msg=f'Something went wrong. Maybe your app is crashed: {str(e)}')
