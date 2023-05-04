import unittest
import requests
import docker


client = docker.from_env()


class TestSuiteWithAsyncTeardown(unittest.IsolatedAsyncioTestCase):
    containers = []
    completed_tests = 0
    # TODO Set the correct number of tests here
    total_tests = 1

    async def async_setUp(self):
        # TODO investigate hardcoded values for names and ports
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
            TestSuiteWithAsyncTeardown.containers.append(container)

    async def async_tearDown(self):
        TestSuiteWithAsyncTeardown.completed_tests += 1
        if TestSuiteWithAsyncTeardown.completed_tests == TestSuiteWithAsyncTeardown.total_tests:
            for container in self.containers:
                container.stop()
                container.remove()
            client.close()

    async def test_get(self):
        await self.async_setUp()
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
            if isinstance(e, AssertionError):
                await self.async_tearDown()
                self.fail(msg=f"Unexpected response, {str(e)}")
            else:
                await self.async_tearDown()
                self.fail(msg='Something went wrong. Try restarting Docker')
        await self.async_tearDown()


