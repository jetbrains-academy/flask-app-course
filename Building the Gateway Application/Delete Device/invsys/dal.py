import shelve
from flask import g


# This function creates a database if none has yet been created,
# or opens it if it's already there.
def pull_db():
    db_ = getattr(g, '_database', None)
    if db_ is None:
        db_ = g._database = shelve.open("storage")
    return db_


# This function returns the entire dataset of devices as a dictionary
def get():
    with pull_db() as shelf:
        keys = list(shelf.keys())
        devices_ = {}
        for key in keys:
            devices_[key] = shelf[key]
    return devices_


# This function adds a new element to the datastore of devices
def post(args):
    with pull_db() as shelf:
        shelf[args['id']] = args
        return shelf[args['id']]


# This function retrieves an item by its identifier and returns it
def get_device(identifier):
    with pull_db() as shelf:
        if not (identifier in shelf):
            return None
        return shelf[identifier]


# This function should update an item in the database, access the item by its id.
# Return None if the identifier is not found.
def put_device(identifier, args):
    with pull_db() as shelf:
        if not (identifier in shelf):
            return None
        device = shelf[identifier]

        # Loop through all the passed arguments and their values (it's like a dictionary).
        # For each argument value, check if it is not empty (None).
        # If not, update the corresponding argument value of the
        # corresponding device with the value provided in the request.
        for k, v in args.items():
            if v is not None:
                device[k] = v
        # Re-assign the new value of device to the identifier in shelve to save changes.
        shelf[identifier] = device
        return shelf[identifier]


# This function should delete an item by its identifier.
# Return None if the identifier is not found.
def delete_device(identifier):
    with pull_db() as shelf:
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
with shelve.open('storage') as db:
    for key, value, in devices.items():
        db[key] = value
