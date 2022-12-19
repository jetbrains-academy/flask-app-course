import unittest
import requests
import time
import aiodocker
import docker


async def run_containers():
    async_docker = aiodocker.Docker()
    docker_client = docker.client.from_env()
    try:
        container_to_restart_invsys = await async_docker.containers.get("flask-app-invsys")
        await container_to_restart_invsys.restart(timeout=0)
    except aiodocker.exceptions.DockerError as e:
        docker_client.containers.run("flask-app-invsys-img", name="flask-app-invsys",  detach=True)
    try:
        container_to_restart_gateway = await async_docker.containers.get("flask-app-gateway")
        await container_to_restart_gateway.restart(timeout=0)
    except aiodocker.exceptions.DockerError as e:
        docker_client.containers.run("flask-app-gateway-img", name="flask-app-gateway", detach=True)

    # TODO the sleep time is arbitrary ATM, it should be adjusted somehow
    time.sleep(0.5)
    await async_docker.close()
    docker_client.close()


async def delete_containers():
    async_docker = aiodocker.Docker()
    try:
        container_to_kill_invsys = await async_docker.containers.get("flask-app-invsys")
        await container_to_kill_invsys.kill(timeout=0)
        await container_to_kill_invsys.delete(timeout=0)
    except aiodocker.exceptions.DockerError as e:
        print(e.message)

    try:
        container_to_kill_gateway = await async_docker.containers.get("flask-app-gateway")
        await container_to_kill_gateway.kill(timeout=0)
        await container_to_kill_gateway.delete(timeout=0)
    except aiodocker.exceptions.DockerError as e:
        print(e.message)
    # TODO the sleep time is arbitrary ATM, it should be adjusted somehow
    time.sleep(0.5)
    await async_docker.close()


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

    def test_post(self):
        # device_id = ''.join(random.choices(string.ascii_lowercase, k=10))
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
        self.addCleanup(self.on_cleanup)
