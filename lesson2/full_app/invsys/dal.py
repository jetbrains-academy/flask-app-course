from flask import g
import shelve

# def teardown_db():
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()


def pull_db():
    db_ = getattr(g, '_database', None)
    if db_ is None:
        db_ = g._database = shelve.open("storage.db")
    return db_


def get():
    with pull_db() as shelf:
        keys = list(shelf.keys())
        devices_ = []
        for key in keys:
            devices_.append(shelf[key])
    return devices_


def get_device(identifier):
    with pull_db() as shelf:
        shelf = pull_db()
        if not (identifier in shelf):
            return None
    return shelf[identifier]


def put_device(identifier, args):
    with pull_db() as shelf:
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


def post(args):
    with pull_db() as shelf:
        shelf[args['id']] = args
        return shelf[args['id']]


def delete_device(identifier):
    with pull_db() as shelf:
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
    #
    # db[devices[0]["id"]] = devices[0]
    # db[devices[1]["id"]] = devices[1]

