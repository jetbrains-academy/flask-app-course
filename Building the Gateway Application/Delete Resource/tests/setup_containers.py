import asyncio

import docker
import aiodocker


async def delete_containers():
    async_docker = aiodocker.Docker()
    docker_client = docker.client.from_env()


    try:
        container_invsys = await async_docker.containers.get("flask-app-invsys")
        await container_invsys.delete(timeout=0)
    except aiodocker.exceptions.DockerError as e:
        print(e.message)

    try:
        container_gateway = await async_docker.containers.get("flask-app-gateway")
        await container_gateway.delete(timeout=0)
    except aiodocker.exceptions.DockerError as e:
        print(e.message)
    docker_client.close()
    await async_docker.close()


async def stop_containers():
    async_docker = aiodocker.Docker()
    try:
        container_invsys = await async_docker.containers.get("flask-app-invsys")
        await container_invsys.kill(timeout=0)
    except aiodocker.exceptions.DockerError as e:
        print(e.message)
    try:
        container_gateway = await async_docker.containers.get("flask-app-gateway")
        await container_gateway.kill(timeout=0)
    except aiodocker.exceptions.DockerError as e:
        print(e.message)
    await async_docker.close()


if __name__ == "__main__":
    asyncio.run(stop_containers())
    asyncio.run(delete_containers())
