import shelve
from flask import g


# This function creates a database if none has yet been created,
# or opens it if it's already there.
def pull_db():
    db_ = getattr(g, '_database', None)
    if db_ is None:
        db_ = g._database = shelve.open("storage.db")
    return db_


# This function returns the entire dataset of devices as a dictionary
def get():
    shelf = pull_db()
    keys = list(shelf.keys())
    devices_ = {}
    for key in keys:
        devices_[key] = shelf[key]
    return devices_


# This function adds a new element to the datastore of devices
def post(args):
    shelf = pull_db()
    shelf[args['id']] = args
    return shelf[args['id']]


# This function retrieves an item by its identifier and returns it
def get_device(identifier):
    shelf = pull_db()

    if not (identifier in shelf):
        return None
    return shelf[identifier]


# This function should update an item in the database, access the item by its id.
# Return None if the identifier is not found.
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
    # Re-assign the new value of device to the identifier in shelve to save changes.
    shelf[identifier] = device
    return shelf[identifier]


# This function should delete an item by its identifier.
# Return None if the identifier is not found.
def delete_device(identifier):
    shelf = pull_db()
    # if the key does not exist on the shelf, return a 404 error.
    if not (identifier in shelf):
        return None
    del shelf[identifier]
    return {'message': f'{identifier} deleted'}


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

