import asyncio
import unittest
import requests
import docker

client = docker.from_env()


class TestSuiteWithAsyncTeardown(unittest.IsolatedAsyncioTestCase):
    containers = []
    completed_tests = 0
    total_tests = 2

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

    async def test_delete_404(self):
        await self.async_setUp()
        try:
            response = requests.delete('http://127.0.0.1:5001/items/100')

            print(response.status_code)
            # TODO this turns out really bad in case of 500 response - several screens of bs html in the console
            print(response.text)
            self.assertEqual(404, response.status_code,
                             msg=f"DELETE request resulted in an unexpected response code: {response.status_code}")
            self.assertEqual(b'{\n  "data": {}, \n  "message": "Device not found"\n}\n'.decode("utf-8").replace(" ", ""),
                             response.content.decode("utf-8").replace(" ", ""),
                             msg="DELETE request resulted in unexpected response content.")
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
        # Here the asyncSetUp() takes place
        try:
            response = requests.delete('http://127.0.0.1:5001/items/002')

            print(response.status_code)
            # TODO this turns out really bad in case of 500 response - several screens of bs html in the console
            print(response.text)
            self.assertEqual(201, response.status_code,
                             msg=f"DELETE request resulted in an unexpected response code: {response.status_code}")
            self.assertEqual(b'{\n  "deleted device": "002"\n}\n'.decode("utf-8").replace(" ", ""),
                             response.content.decode("utf-8").replace(" ", ""),
                             msg="DELETE request resulted in unexpected response content.")
        except Exception as e:
            if isinstance(e, AssertionError):
                await self.async_tearDown()
                self.fail(msg=f"Unexpected response, {str(e)}")
            else:
                await self.async_tearDown()
                self.fail(msg='Something went wrong. Try restarting Docker')
        await self.async_tearDown()
