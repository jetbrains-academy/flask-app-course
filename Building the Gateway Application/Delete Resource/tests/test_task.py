import unittest
import requests
import aiodocker
import docker


class TestCase(unittest.IsolatedAsyncioTestCase):
    container_invsys = None
    container_gateway = None
    async_docker = None
    docker_client = None

    async def run_containers(self):
        if self.async_docker is None:
            self.async_docker = aiodocker.Docker()
        if self.docker_client is None:
            self.docker_client = docker.client.from_env()
        try:
            self.container_invsys = await self.async_docker.containers.get("flask-app-invsys")
            await self.container_invsys.restart(timeout=0)
        except aiodocker.exceptions.DockerError as e:
            self.container_invsys = self.docker_client.containers.run("flask-app-invsys-img", name="flask-app-invsys",  detach=True)
            pass
        try:
            self.container_gateway = await self.async_docker.containers.get("flask-app-gateway")
            await self.container_gateway.restart(timeout=0)
        except aiodocker.exceptions.DockerError as e:
            self.container_gateway = self.docker_client.containers.run("flask-app-gateway-img", name="flask-app-gateway", detach=True)
            pass

    async def delete_containers(self):
        async_docker = self.async_docker

        try:
            self.container_invsys = await async_docker.containers.get("flask-app-invsys")
            await self.container_invsys.delete(timeout=0)
        except aiodocker.exceptions.DockerError as e:
            print(e.message)

        try:
            self.container_gateway = await async_docker.containers.get("flask-app-gateway")
            await self.container_gateway.delete(timeout=0)
        except aiodocker.exceptions.DockerError as e:
            print(e.message)
        self.docker_client.close()
        await async_docker.close()

    async def stop_containers(self):
        async_docker = self.async_docker
        try:
            self.container_invsys = await async_docker.containers.get("flask-app-invsys")
            await self.container_invsys.kill(timeout=0)
        except aiodocker.exceptions.DockerError as e:
            print(e.message)
        try:
            self.container_gateway = await async_docker.containers.get("flask-app-gateway")
            await self.container_gateway.kill(timeout=0)
        except aiodocker.exceptions.DockerError as e:
            print(e.message)

    async def asyncSetUp(self):
        await self.run_containers()
        print("Running test instances")

    async def asyncTearDown(self) -> None:
        await self.stop_containers()
        print("Stopped test instances")

    async def on_cleanup(self):
        await self.delete_containers()

    async def test_delete_404(self):
        response = requests.delete('http://127.0.0.1:5001/items/100')

        print(response.status_code)
        # TODO this turns out really bad in case of 500 response - several screens of bs html in the console
        print(response.text)
        self.assertEqual(404, response.status_code, msg=f"DELETE request resulted in an unexpected response code: {response.status_code}")
        self.assertEqual(b'{\n  "data": {}, \n  "message": "Device not found"\n}\n'.decode("utf-8").replace(" ", ""),
                         response.content.decode("utf-8").replace(" ", ""),
                         msg="DELETE request resulted in unexpected response content.")
        # This should be added to the last running test, 1 per Test Case (Task)
        self.addAsyncCleanup(self.on_cleanup)

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

