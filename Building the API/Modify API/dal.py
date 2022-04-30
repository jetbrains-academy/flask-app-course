import shelve
from flask import g


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


def get_device(identifier):
    shelf = pull_db()

    if not (identifier in shelf):
        return None
    return shelf[identifier]


def put_device(identifier, args):
    shelf = pull_db()
    if not (identifier in shelf):
        return None
    device = shelf[identifier]
    # Loop Through all the passed arguments
    for k, v in args.items():
        # Check if the passed value is not null
        if v is not None:
            # if not, set the element in the devices dict with the 'k' object to the value provided in the request.
            device[k] = v
    shelf[identifier] = device
    return shelf[identifier]


def delete_device(identifier):
    shelf = pull_db()
    # If the key does not exist on the shelf, return None.
    if not (identifier in shelf):
        return None
    del shelf[identifier]
    return {'message': f'{identifier} deleted'}


# A Dict of Dicts to define initial devices
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
with shelve.open('storage.db') as db:
    for key, value, in devices.items():
        db[key] = value
