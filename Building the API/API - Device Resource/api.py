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
    def get(self, identifier):
        try:
            device = devices[identifier]

        except KeyError:
            return self.not_found_response

        # Construct a response object that consists of a json object and a response code:
        return flask.make_response(jsonify({"device": device}), 200,)

    # PUT - Given an id
    def put(self, identifier):
        args = self.reqparse.parse_args()
        if identifier not in devices.keys():
            return self.not_found_response

        # Loop through all the passed arguments and their values (it's like a dictionary).
        # For each argument value, check if it is not empty (None).
        # If not, update the corresponding argument value of the
        # corresponding device with the value provided in the request:
        for k, v in args.items():
            if v is not None:
                devices[identifier][k] = v

        return flask.make_response(jsonify({"updated device": devices[identifier]}), 200,)

    # Delete - Given an id
    def delete(self, identifier):
        if identifier not in devices.keys():
            return self.not_found_response
        del devices[identifier]
        return flask.make_response(jsonify({"deleted device": identifier}), 201,)


# Now we can add endpoints and run the app.
api.add_resource(Device, "/items/<string:identifier>")

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)