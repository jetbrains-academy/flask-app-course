import asyncio
import unittest
import requests
import docker

client = docker.from_env()

class TestSuiteWithAsyncTeardown(unittest.IsolatedAsyncioTestCase):
    containers = []
    completed_tests = 0
    total_tests = 1

    async def async_setUp(self):
        self.container_names = ["flask-app-invsys", "flask-app-gateway"]
        self.image_names = ["flask-app-invsys-img", "flask-app-gateway-img"]
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
                await asyncio.sleep(5)  # Give some time for the container to start
            print("len on setup is" + str(len(TestSuiteWithAsyncTeardown.containers)))
            TestSuiteWithAsyncTeardown.containers.append(container)

    async def async_tearDown(self):
        TestSuiteWithAsyncTeardown.completed_tests += 1
        if TestSuiteWithAsyncTeardown.completed_tests == TestSuiteWithAsyncTeardown.total_tests:
            for container in self.containers:
                container.stop()
                container.remove()
            client.close()

    async def test_post(self):
        await self.async_setUp()
        response = requests.post('http://127.0.0.1:5001/items', json={"id": "New_device_ID",
                                                                      "name": "UPDATE",
                                                                      "location": "location",
                                                                      "status": "off"})
        print(response.status_code)
        print(response.text)
        self.assertEqual(201, response.status_code, msg="POST request resulted in an unexpected response status code.")
        self.assertEqual((b'{\n  "device": {\n    "id": "New_device_ID", \n    "location": "location", \n  '
                          b'  "name": "UPDATE", \n    "status": "off"\n  }\n}\n').decode("utf-8").replace(" ", ""),
                         response.content.decode("utf-8").replace(" ", ""),
                         msg="POST request resulted in an unexpected response content.")
        await self.async_tearDown()
