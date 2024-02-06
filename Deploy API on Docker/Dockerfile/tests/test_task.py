import asyncio
import unittest
import requests
import docker
import random
import string


client = docker.from_env()


class TestSuiteWithAsyncTeardown(unittest.IsolatedAsyncioTestCase):
    containers = []
    completed_tests = 0
    # TODO Set the correct number of tests here
    total_tests = 4

    async def async_setUp(self):
        # TODO investigate hardcoded values for names and ports
        self.container_names = ["flask-app-invsys"]
        self.image_names = ["flask-app-invsys-img"]
        self.container_ports = [None, 5001]
        self.host_ports = [None, 5001]

        TestSuiteWithAsyncTeardown.containers = []

        for idx, container_name in enumerate(self.container_names):
            container_list = client.containers.list(filters={'name': container_name})
            if container_list:
                container = container_list[0]
                if container.status != 'running':
                    container.restart()
            else:
                if self.container_ports[idx] is not None:
                    container = client.containers.run(self.image_names[idx], name=container_name,
                                                      ports={f'{self.container_ports[idx]}/tcp': self.host_ports[idx]},
                                                      detach=True)
                else:
                    container = client.containers.run(self.image_names[idx], name=container_name, detach=True)
            TestSuiteWithAsyncTeardown.containers.append(container)

    async def async_tearDown(self):
        TestSuiteWithAsyncTeardown.completed_tests += 1
        if TestSuiteWithAsyncTeardown.completed_tests == TestSuiteWithAsyncTeardown.total_tests:
            for container in self.containers:
                container.stop()
                container.remove()
            for image_name in self.image_names:
                client.images.remove(image_name)
            client.close()

# teardown to remove ALL images:
    # async def async_tearDown(self):
    #     TestSuiteWithAsyncTeardown.completed_tests += 1
    #     if TestSuiteWithAsyncTeardown.completed_tests == TestSuiteWithAsyncTeardown.total_tests:
    #         client = docker.from_env()
    #
    #         # Stop and remove all containers
    #         for container in client.containers.list(all=True):
    #             container.stop()
    #             container.remove(force=True)
    #
    #         # Remove all images
    #         for image in client.images.list():
    #             client.images.remove(image.id, force=True)
    #
    #         client.close()


    async def test_post(self):
        await self.async_setUp()
        try:
            device_id = ''.join(random.choices(string.ascii_lowercase, k=10))
            response = requests.post('http://127.0.0.1:5000/items', json={"id": f"{device_id}",
                                                                          "name": "UPDATEDUPDATEDUPDATED",
                                                                          "location": "location",
                                                                          "status": "off"})
            print(response.status_code)
            print(response.text)
            self.assertEqual(201, response.status_code, msg=f"Unexpected response code {response.status_code}")
        except Exception as e:
            if type(e) == AssertionError:
                await self.async_tearDown()
                self.fail(msg=f"Unexpected response, {str(e)}")
            else:
                await self.async_tearDown()
                self.fail(msg='Something went wrong. Try restarting Docker')

        await self.async_tearDown()

    async def test_get(self):
        await self.async_setUp()
        try:
            response = requests.get('http://127.0.0.1:5000/items')
            print(response.status_code)
            print(response.text)
            self.assertEqual(200, response.status_code, msg=f"GET request resulted in an unexpected response code: {response.status_code}")

        except Exception as e:
            if isinstance(e, AssertionError):
                await self.async_tearDown()
                self.fail(msg=f"Unexpected response, {str(e)}")
            else:
                await self.async_tearDown()
                self.fail(msg='Something went wrong. Try restarting Docker')
        await self.async_tearDown()

    async def test_put(self):
        await self.async_setUp()
        try:
            # device_id = ''.join(random.choices(string.ascii_lowercase, k=10))
            response = requests.put('http://127.0.0.1:5000/items/002', json={"id": "002",
                                                                             "name": "Humidity_sensor",
                                                                             "location": "bedroom",
                                                                             "status": "off"})
            print(response.status_code)
            print(response.text)
            self.assertEqual(200, response.status_code, msg=f"PUT request resulted in an unexpected response code: {response.status_code}")

        except Exception as e:
            if isinstance(e, AssertionError):
                await self.async_tearDown()
                self.fail(msg=f"Unexpected response, {str(e)}")
            else:
                await self.async_tearDown()
                self.fail(msg='Something went wrong. Try restarting Docker')
        await self.async_tearDown()

    async def test_delete(self):
        await self.async_setUp()
        try:
            response = requests.delete('http://127.0.0.1:5000/items/100')
            print(response.status_code)
            print(response.text)
            self.assertEqual(404, response.status_code, msg=f"DELETE request resulted in an unexpected response code: {response.status_code}")

        except Exception as e:
            if isinstance(e, AssertionError):
                await self.async_tearDown()
                self.fail(msg=f"Unexpected response, {str(e)}")
            else:
                await self.async_tearDown()
                self.fail(msg='Something went wrong. Try restarting Docker')
        await self.async_tearDown()
