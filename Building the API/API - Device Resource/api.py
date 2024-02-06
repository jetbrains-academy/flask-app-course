from flask import Flask, request, jsonify
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)

# Dictionary to mimic the database
devices = {
    "001": {"id": "001", "name": "Light bulb", "location": "hall", "status": "off"},
    "002": {"id": "002", "name": "Humidity sensor", "location": "bedroom", "status": "on"},
    "003": {"id": "003", "name": "Humidifier", "location": "bedroom", "status": "off"}
}


# Define Marshmallow Schema for request and response validation
class DeviceSchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str(required=True)
    location = fields.Str(required=True)
    status = fields.Str(required=True)


device_schema = DeviceSchema()

@app.route('/items/<string:identifier>', methods=['GET', 'PUT', 'DELETE'])
def device(identifier):
    if request.method == 'GET':
        device = devices.get(identifier)
        if not device:
            return jsonify({'message': 'Device not found'}), 404
        return jsonify(device), 200

    elif request.method == 'PUT':
        try:
            args = device_schema.load(request.json, partial=True)
        except ValidationError as err:
            return jsonify(err.messages), 400

        if identifier not in devices:
            return jsonify({'message': 'Device not found'}), 404

        devices[identifier].update(args)
        return jsonify({"updated device": identifier}), 200

    elif request.method == 'DELETE':
        if identifier not in devices:
            return jsonify({'message': 'Device not found'}), 404
        del devices[identifier]
        return jsonify({'message': 'Device deleted'}), 200


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)

# import flask
# from flask import Flask, jsonify
# from flask_restful import Resource, Api, reqparse
#
# # Initialize Flask
# app = Flask(__name__)
# api = Api(app)
#
# devices = {"001": {
#     "id": "001",
#     "name": "Light bulb",
#     "location": "hall",
#     "status": "off"
# },
#     "002": {
#         "id": "002",
#         "name": "Humidity_sensor",
#         "location": "bedroom",
#         "status": "on"
#     },
#     "003": {
#         "id": "003",
#         "name": "Humidifier",
#         "location": "bedroom",
#         "status": "off"
#     }
# }
#
#
# # Resource: Individual Device Routes
# class Device(Resource):
#     def __init__(self):
#         # Initialize The Flask Request Parser and add arguments as in an expected request
#         self.reqparse = reqparse.RequestParser()
#         self.reqparse.add_argument("id", type=str, location="json")
#         self.reqparse.add_argument("name", type=str, location="json")
#         self.reqparse.add_argument("location", type=str, location="json")
#         self.reqparse.add_argument("status", type=str, location="json")
#         self.not_found_response = flask.make_response(jsonify({'message': 'Device not found', 'data': {}}), 404,)
#
#         super(Device, self).__init__()
#
#     # GET - Returns a single device object given a matching id
#     def get(self, identifier):
#         try:
#             device = devices[identifier]
#
#         except KeyError:
#             return self.not_found_response
#
#         # Construct a response object that consists of a json object and a response code:
#         return flask.make_response(jsonify({"device": device}), 200,)
#
#     # PUT - Given an id
#     def put(self, identifier):
#         args = self.reqparse.parse_args()
#         if identifier not in devices.keys():
#             return self.not_found_response
#
#         # Loop through all the passed arguments and their values (it's like a dictionary).
#         # For each argument value, check if it is not empty (None).
#         # If not, update the corresponding argument value of the
#         # corresponding device with the value provided in the request:
#         for k, v in args.items():
#             if v is not None:
#                 devices[identifier][k] = v
#
#         return flask.make_response(jsonify({"updated device": devices[identifier]}), 200,)
#
#     # Delete - Given an id
#     def delete(self, identifier):
#         if identifier not in devices.keys():
#             return self.not_found_response
#         del devices[identifier]
#         return flask.make_response(jsonify({"deleted device": identifier}), 201,)
#
#
# # Now we can add endpoints and run the app.
# api.add_resource(Device, "/items/<string:identifier>")
#
# if __name__ == "__main__":
#     app.run("0.0.0.0", port=5000, debug=True)