import unittest

from task import port_available


class TestCase(unittest.TestCase):
    def test_5000(self):
        self.assertTrue(port_available(5000), msg="Checking port 5000: Failed")

    def test_5001(self):
        self.assertTrue(port_available(5001), msg="Checking port 5001: Failed")
