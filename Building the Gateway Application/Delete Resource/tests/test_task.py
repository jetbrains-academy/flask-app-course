import unittest
import requests
import time
import aiodocker


async def run_containers():
    async_docker = aiodocker.Docker()
    # We only restart the invsys ATM, it might not allways be the case
    print('== Restarting the instance of invsys container ==')
    container_to_restart_invsys = await async_docker.containers.get("flask-app-invsys")
    await container_to_restart_invsys.restart(timeout=0)
    # TODO the sleep time is arbitrary ATM, it should be adjusted somehow
    time.sleep(0.5)
    await async_docker.close()


class TestCase(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self._async_connection = await run_containers()

    async def test_delete_404(self):
        # Here the asyncSetUp() takes place
        response = requests.delete('http://127.0.0.1:5001/items/100')

        print(response.status_code)
        # TODO this turns out really bad in case of 500 response - several screens of bs html in the console
        print(response.text)
        self.assertEqual(404, response.status_code, msg=f"DELETE request resulted in an unexpected response code: {response.status_code}")
        self.assertEqual(b'{\n  "data": {}, \n  "message": "Device not found"\n}\n'.decode("utf-8").replace(" ", ""),
                         response.content.decode("utf-8").replace(" ", ""),
                         msg="DELETE request resulted in unexpected response content.")
        # Here would be the asyncTearDown. I am not sure if we should stop the containers or leave them hanging

    async def test_delete(self):
        # Here the asyncSetUp() takes place
        response = requests.delete('http://127.0.0.1:5001/items/002')

        print(response.status_code)
        # TODO this turns out really bad in case of 500 response - several screens of bs html in the console
        print(response.text)
        self.assertEqual(201, response.status_code,
                         msg=f"DELETE request resulted in an unexpected response code: {response.status_code}")
        self.assertEqual(b'{\n  "deleted device": "002"\n}\n'.decode("utf-8").replace(" ", ""),
                         response.content.decode("utf-8").replace(" ", ""),
                         msg="DELETE request resulted in unexpected response content.")
        # Here would be the asyncTearDown. I am not sure if we should stop the containers or leave them hanging

