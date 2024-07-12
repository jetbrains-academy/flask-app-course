import shelve

devices = {"001": {
    "id": "001",
    "name": "Light bulb",
    "location": "hall",
    "status": "off"
},
    "002": {
        "id": "002",
        "name": "Humidity_sensor",
        "location": "bedroom",
        "status": "on"
    },
    "003": {
        "id": "003",
        "name": "Humidifier",
        "location": "bedroom",
        "status": "off"
    }
}

# Initialize db with some data already in it
with shelve.open('storage') as db:
    # for i, j in enumerate(devices):
    for key, value, in devices.items():
        db[key] = value

if __name__ == '__main__':
    with shelve.open('storage') as db:
        for item in db.items():
            print(item)
