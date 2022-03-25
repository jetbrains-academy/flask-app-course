import shelve

# A List of Dicts to define initial devices
devices = [{
    "id": "001",
    "name": "Light bulb",
    "location": "hall",
    "status": "off"
},
    {
        "id": "002",
        "name": "Humidity_sensor",
        "location": "bedroom",
        "status": "on"
    },
    {
        "id": "003",
        "name": "Humidifier",
        "location": "bedroom",
        "status": "off"
    }
]

# Initialize db with some data already in it
with shelve.open('storage.db') as db:
    for i, j in enumerate(devices):
        db[devices[i]["id"]] = j


