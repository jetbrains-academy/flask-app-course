import subprocess
import time
import unittest
import requests


class TestWithDockerCompose(unittest.IsolatedAsyncioTestCase):
    healthcheck_url = 'http://127.0.0.1:5000'
    @classmethod
    def setUpClass(cls):
        max_retries = 5
        retry_interval = 1
        for retry in range(max_retries):
            try:
                print(f"Checking App on {cls.healthcheck_url} healthcheck_url. Attempt {retry}.")
                response = requests.get(cls.healthcheck_url)
                response.raise_for_status()
                break
            except (requests.RequestException, requests.exceptions.HTTPError):
                time.sleep(retry_interval)
        else:
            print(f"App on {cls.healthcheck_url} did not wake up after {max_retries} attempts.")
        time.sleep(0.5)

    @classmethod
    def tearDownClass(cls):
        subprocess.run(['docker', 'compose', '--project-name', 'flask-course', 'down', '--volumes', '--rmi', 'all'], check=False)
