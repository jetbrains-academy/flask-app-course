import flask
from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import dal

# Initialize Flask
app = Flask(__name__)
api = Api(app)


# Nothing here

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
        device = dal.get_device(identifier)

        if not device:
            return self.not_found_response
        return flask.make_response(jsonify({"device": device}), 200,)

    # PUT - Given an id
    def put(self, identifier):
        args = self.reqparse.parse_args()
        updated_device = dal.put_device(identifier, args)

        if not updated_device:
            return self.not_found_response
        return flask.make_response(jsonify({"updated device": updated_device}), 200,)

    # Delete - Given an id
    def delete(self, identifier):
        deleted = dal.delete_device(identifier)

        if not deleted:
            return self.not_found_response
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
        return flask.make_response(jsonify({"items": dal.get()}), 200,)

    def post(self):
        args = self.reqparse.parse_args()
        posted_device = dal.post(args)
        if not posted_device:
            return 404
        return flask.make_response(jsonify({"device": posted_device}), 201,)


api.add_resource(DeviceInventory, "/items")
api.add_resource(Device, "/items/<string:identifier>")

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
