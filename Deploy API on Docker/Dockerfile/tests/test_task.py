import asyncio
import subprocess
import time
import unittest
import requests
import docker
import random
import string

client = docker.from_env()


class TestSuiteWithAsyncTeardown(unittest.IsolatedAsyncioTestCase):
    healthcheck_url = 'http://127.0.0.1:5000/items'

    @classmethod
    def setUpClass(cls):
        max_retries = 5
        retry_interval = 1
        for retry in range(max_retries):
            try:
                response = requests.get(cls.healthcheck_url)
                response.raise_for_status()
                break
            except (requests.RequestException, requests.exceptions.HTTPError):
                print('fail')
                time.sleep(retry_interval)
        else:
            print(f"App on {cls.healthcheck_url} did not wake up after {max_retries} attempts.")

    @classmethod
    def tearDownClass(cls):
        subprocess.run(['docker', 'compose', 'down', '--volumes', '--rmi', 'all'], check=False)

    async def test_post(self):
        try:
            device_id = ''.join(random.choices(string.ascii_lowercase, k=10))
            response = requests.post('http://127.0.0.1:5000/items', json={"id": f"{device_id}",
                                                                          "name": "UPDATEDUPDATEDUPDATED",
                                                                          "location": "location",
                                                                          "status": "off"})
            print(response.status_code)
            print(response.text)
            self.assertEqual(201, response.status_code,
                             msg=f"POST request resulted in an unexpected response code: {response.status_code}")

        except Exception as e:
            if type(e) == AssertionError:
                self.fail(msg=f"Unexpected response for POST, {str(e)}")
            else:
                self.fail(msg=f'Something went wrong. Maybe your app is crashed: {str(e)}')

    async def test_get(self):
        try:
            response = requests.get('http://127.0.0.1:5000/items')
            print(response.status_code)
            print(response.text)
            self.assertEqual(200, response.status_code,
                             msg=f"GET request resulted in an unexpected response code: {response.status_code}")

        except Exception as e:
            if isinstance(e, AssertionError):
                self.fail(msg=f"Unexpected response for GET, {str(e)}")
            else:
                self.fail(msg=f'Something went wrong. Maybe your app is crashed: {str(e)}')

    async def test_put(self):
        try:
            # device_id = ''.join(random.choices(string.ascii_lowercase, k=10))
            response = requests.put('http://127.0.0.1:5000/items/002', json={"id": "002",
                                                                             "name": "Humidity_sensor",
                                                                             "location": "bedroom",
                                                                             "status": "off"})
            print(response.status_code)
            print(response.text)
            self.assertEqual(200, response.status_code,
                             msg=f"PUT request resulted in an unexpected response code: {response.status_code}")

        except Exception as e:
            if isinstance(e, AssertionError):
                self.fail(msg=f"Unexpected response for PUT, {str(e)}")
            else:
                self.fail(msg=f'Something went wrong. Maybe your app is crashed: {str(e)}')

    async def test_delete(self):
        try:
            response = requests.delete('http://127.0.0.1:5000/items/100')
            print(response.status_code)
            print(response.text)
            self.assertEqual(404, response.status_code,
                             msg=f"DELETE request resulted in an unexpected response code: {response.status_code}")

        except Exception as e:
            if isinstance(e, AssertionError):
                self.fail(msg=f"Unexpected response for DELETE, {str(e)}")
            else:
                self.fail(msg=f'Something went wrong. Maybe your app is crashed: {str(e)}')
