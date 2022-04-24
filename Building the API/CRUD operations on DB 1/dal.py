import shelve
from flask import g


# This function creates a database if none has yet been created,
# or opens it if it's already there.
def pull_db():
    db_ = getattr(g, '_database', None)
    if db_ is None:
        db_ = g._database = shelve.open("storage.db")
    return db_


def get():
    shelf = pull_db()
    keys = list(shelf.keys())
    devices_ = {}
    for key in keys:
        devices_[key] = shelf[key]
    return devices_


def post(args):
    shelf = pull_db()
    shelf[args['id']] = args
    return shelf[args['id']]


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


