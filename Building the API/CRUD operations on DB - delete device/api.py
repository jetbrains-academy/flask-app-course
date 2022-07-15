import flask
from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse

# Initialize Flask
app = Flask(__name__)
api = Api(app)

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


# Resource: Individual Device Routes
class Device(Resource):
    def __init__(self):
        # Initialize The Flask Request Parser and add arguments as in an expected request
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("id", type=str, location="json")
        self.reqparse.add_argument("name", type=str, location="json")
        self.reqparse.add_argument("location", type=str, location="json")
        self.reqparse.add_argument("status", type=str, location="json")
        self.not_found_response = flask.make_response(jsonify({'message': 'Device not found', 'data': {}}), 404,)

        super(Device, self).__init__()

    # GET - Returns a single device object given a matching id
    # @staticmethod
    def get(self, identifier):
        device = devices[identifier]

        if not device:
            return self.not_found_response

        return flask.make_response(jsonify({"device": device}), 200,)

    # PUT - Given an id
    def put(self, identifier):
        args = self.reqparse.parse_args()
        # Return an error message and a 404 code if the identifier wasn't found.
        if identifier not in devices.keys():
            return self.not_found_response

        # Loop through all the passed arguments and their values (it's like a dictionary).
        # For each argument value, check if it is not empty (None).
        # If not, update the corresponding argument value of the
        # corresponding device with the value provided in the request.
        for k, v in args.items():
            if v is not None:
                devices[identifier][k] = v

        return flask.make_response(jsonify({"updated device": devices[identifier]}), 200,)

    # Delete - Given an id
    # @staticmethod
    def delete(self, identifier):
        if identifier not in devices.keys():
            return self.not_found_response
        del devices[identifier]
        return flask.make_response(jsonify({"deleted device": identifier}), 201,)


class DeviceInventory(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            "id", type=str, required=True, help="Device id must be provided", location="json")
        self.reqparse.add_argument(
            "name", type=str, required=True, help="Device name must be provided", location="json")
        self.reqparse.add_argument(
            "location", type=str, required=True, help="Device location must be provided", location="json")
        self.reqparse.add_argument("status", type=str, required=True,
                                   help="Device status must be provided", location="json")

        super(DeviceInventory, self).__init__()

    @staticmethod
    def get():
        return flask.make_response(jsonify({"items": devices}), 200,)

    def post(self):
        args = self.reqparse.parse_args()
        devices[args["id"]] = args

        return flask.make_response(jsonify({"Posted a device": args}), 201,)


# Now we can add endpoints and run the app.
api.add_resource(DeviceInventory, "/items")
api.add_resource(Device, "/items/<string:identifier>")

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)