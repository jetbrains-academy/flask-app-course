from flask import Flask, request, jsonify
from marshmallow import Schema, fields, ValidationError, validates_schema
import dal

app = Flask(__name__)


# Define Marshmallow Schema for request and response validation
class DeviceSchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str(required=True)
    location = fields.Str(required=True)
    status = fields.Str(required=True)

    #Use validates_schema for custom validation logic
    @validates_schema(pass_original=True)
    def validate_required_fields(self, data, original_data, **kwargs):
        required_fields = ['id', 'name', 'location', 'status']
        if request.method == 'POST':
            for field in required_fields:
                if field not in original_data:
                    raise ValidationError(f'{field} is required.', field)

# Instantiate the schemas
device_schema = DeviceSchema()
devices_schema = DeviceSchema(many=True)  # For multiple devices


@app.route('/items/<string:identifier>', methods=['GET', 'PUT', 'DELETE'])
def device(identifier):
    if request.method == 'GET':
        device = dal.get_device(identifier)
        if not device:
            return jsonify({'message': 'Device not found'}), 404
        return device_schema.dump(device)

    elif request.method == 'PUT':
        try:
            args = device_schema.load(request.json, partial=True)  # Allow partial updates
        except ValidationError as err:
            return jsonify(err.messages), 400

        updated_device = dal.put_device(identifier, args)
        if not updated_device:
            return jsonify({'message': 'Device not found'}), 404

        return jsonify({"updated device": identifier}), 200

    elif request.method == 'DELETE':
        deleted = dal.delete_device(identifier)
        if not deleted:
            return jsonify({'message': 'Device not found'}), 404
        return jsonify({'message': 'Device deleted'}), 200


@app.route('/items', methods=['GET', 'POST'])
def device_inventory():
    if request.method == 'GET':
        devices = dal.get()
        return jsonify(devices_schema.dump(devices))

    elif request.method == 'POST':
        try:
            args = device_schema.load(request.json)
        except ValidationError as err:
            return jsonify(err.messages), 400
        new_device = dal.post(args)
        if not new_device:
            return jsonify({'message': 'Device could not be added'}), 404
        return jsonify({"Posted a device": device_schema.dump(new_device)}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


# import flask
# from flask import Flask, jsonify
# from flask_restful import Resource, Api, reqparse
# import dal
#
# # Initialize Flask
# app = Flask(__name__)
# api = Api(app)
#
#
# # Nothing here
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
#     # @staticmethod
#     def get(self, identifier):
#         device = dal.get_device(identifier)
#
#         if not device:
#             return self.not_found_response
#         # return {"device": device}
#         return flask.make_response(jsonify({"device": device}), 200,)
#
#     # PUT - Given an id
#     def put(self, identifier):
#         args = self.reqparse.parse_args()
#         updated_device = dal.put_device(identifier, args)
#
#         if not updated_device:
#             return self.not_found_response
#         # return {"updated device": updated_device}
#         return flask.make_response(jsonify({"updated device": updated_device}), 200,)
#
#     # Delete - Given an id
#     # @staticmethod
#     def delete(self, identifier):
#         deleted = dal.delete_device(identifier)
#
#         if not deleted:
#             return self.not_found_response
#         # return deleted, 201
#         return flask.make_response(jsonify({"deleted device": identifier}), 201,)
#
#
# class DeviceInventory(Resource):
#     def __init__(self):
#         self.reqparse = reqparse.RequestParser()
#         self.reqparse.add_argument(
#             "id", type=str, required=True, help="Device id must be provided", location="json")
#         self.reqparse.add_argument(
#             "name", type=str, required=True, help="Device name must be provided", location="json")
#         self.reqparse.add_argument(
#             "location", type=str, required=True, help="Device location must be provided", location="json")
#         self.reqparse.add_argument("status", type=str, required=True,
#                                    help="Device status must be provided", location="json")
#
#         super(DeviceInventory, self).__init__()
#
#     @staticmethod
#     def get():
#         # return dal.get()
#         return flask.make_response(jsonify({"items": dal.get()}), 200,)
#
#     def post(self):
#         args = self.reqparse.parse_args()
#         posted_device = dal.post(args)
#         if not posted_device:
#             return 404
#         #return {"device": posted_device}, 201
#         return flask.make_response(jsonify({"device": posted_device}), 201,)
#
#
# api.add_resource(DeviceInventory, "/items")
# api.add_resource(Device, "/items/<string:identifier>")
#
# if __name__ == "__main__":
#     app.run("0.0.0.0", port=5000, debug=True)
