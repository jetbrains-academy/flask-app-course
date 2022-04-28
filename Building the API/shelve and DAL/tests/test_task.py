import unittest
import shelve

import dal


class TestCase(unittest.TestCase):
    def test_db(self):
        devices = [('002', {'id': '002', 'name': 'Humidity_sensor', 'location': 'bedroom', 'status': 'on'}),
                ('001', {'id': '001', 'name': 'Light bulb', 'location': 'hall', 'status': 'off'}),
                ('003', {'id': '003', 'name': 'Humidifier', 'location': 'bedroom', 'status': 'off'})]
        with shelve.open('storage.db') as db:
            for device in devices:
                self.assertTrue(device in db.items(), msg='Database looks incomplete')