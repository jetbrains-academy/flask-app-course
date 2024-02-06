from flask import Flask, request, jsonify
from marshmallow import Schema, fields, ValidationError, EXCLUDE
import dal

app = Flask(__name__)


# Define Marshmallow Schemas for request and response validation
class DeviceSchema(Schema):
    id = fields.Str()
    name = fields.Str()
    location = fields.Str()
    status = fields.Str()


# For POST requests where all fields are required
class DevicePostSchema(DeviceSchema):
    id = fields.Str(required=True)
    name = fields.Str(required=True)
    location = fields.Str(required=True)
    status = fields.Str(required=True)


# For PUT requests where NOT all fields are required
class DeviceUpdateSchema(Schema):
    name = fields.Str(required=False)
    location = fields.Str(required=False)
    status = fields.Str(required=False)

    class Meta:
        unknown = EXCLUDE


# Instantiate the schemas
device_schema = DeviceSchema()
devices_schema = DeviceSchema(many=True)  # For multiple devices
device_post_schema = DevicePostSchema()
device_update_schema = DeviceUpdateSchema()


@app.route('/items/<string:identifier>', methods=['GET', 'PUT', 'DELETE'])
def device(identifier):
    if request.method == 'GET':
        device = dal.get_device(identifier)
        if not device:
            return jsonify({'message': 'Device not found'}), 404
        return device_schema.dump(device)

    elif request.method == 'PUT':
        try:
            args = device_update_schema.load(request.json, partial=True)  # Allow partial updates
        except ValidationError as err:
            return jsonify(err.messages), 400

        # Since the 'id' field is now excluded from validation, it won't cause an error
        updated_device = dal.put_device(identifier, args)
        if not updated_device:
            return jsonify({'message': 'Device not found'}), 404

        return jsonify(device_schema.dump(updated_device)), 200

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
            args = device_post_schema.load(request.json)
        except ValidationError as err:
            return jsonify(err.messages), 400
        new_device = dal.post(args)
        if not new_device:
            return jsonify({'message': 'Device could not be added'}), 404
        return jsonify(device_schema.dump(new_device)), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

# from flask import Flask, request
# from flask_restful import Resource, Api
# import dal
# from marshmallow import Schema, fields, ValidationError
#
# # Initialize Flask
# app = Flask(__name__)
# api = Api(app)
#
# # Marshmallow Schemas
# class DeviceSchema(Schema):
#     id = fields.Str()
#     name = fields.Str()
#     location = fields.Str()
#     status = fields.Str()
#
# # For POST and PUT requests where all fields are required
# class DevicePostPutSchema(DeviceSchema):
#     id = fields.Str(required=True)
#     name = fields.Str(required=True)
#     location = fields.Str(required=True)
#     status = fields.Str(required=True)
#
# device_schema = DeviceSchema()
# device_post_put_schema = DevicePostPutSchema()
#
# # Resource: Individual Device Routes
# class Device(Resource):
#     # GET - Returns a single device object given a matching id
#     def get(self, identifier):
#         device = dal.get_device(identifier)
#         if not device:
#             return {'message': 'Device not found', 'data': {}}, 404
#         return {"device": device}
#
#     # PUT - Given an id
#     def put(self, identifier):
#         try:
#             args = device_post_put_schema.load(request.json)
#         except ValidationError as err:
#             return err.messages, 400
#
#         updated_device = dal.put_device(identifier, args)
#         if not updated_device:
#             return {'message': 'Device not found', 'data': {}}, 404
#         return {"updated device": updated_device}
#
#     # Delete - Given an id
#     @staticmethod
#     def delete(identifier):
#         deleted = dal.delete_device(identifier)
#         if not deleted:
#             return {'message': 'Device not found', 'data': {}}, 404
#         return deleted, 201
#
# class DeviceInventory(Resource):
#     @staticmethod
#     def get():
#         return dal.get()
#
#     def post(self):
#         try:
#             args = device_post_put_schema.load(request.json)
#         except ValidationError as err:
#             return err.messages, 400
#
#         posted_device = dal.post(args)
#         if not posted_device:
#             return {'message': 'Device not found', 'data': {}}, 404
#         return {"device": posted_device}, 201
#
# # Adding resources to API
# api.add_resource(DeviceInventory, "/items")
# api.add_resource(Device, "/items/<string:identifier>")
#
# if __name__ == "__main__":
#     app.run("0.0.0.0", port=5000, debug=True)

#
#
# # from flask import Flask
# # from flask_restful import Resource, Api, reqparse
# # import dal
# #
# # # Initialize Flask
# # app = Flask(__name__)
# # api = Api(app)
# #
# #
# # # Resource: Individual Device Routes
# # class Device(Resource):
# #     def __init__(self):
# #         # Initialize The Flask Request Parser and add arguments as in an expected request
# #         self.reqparse = reqparse.RequestParser()
# #         self.reqparse.add_argument("id", type=str, location="json")
# #         self.reqparse.add_argument("name", type=str, location="json")
# #         self.reqparse.add_argument("location", type=str, location="json")
# #         self.reqparse.add_argument("status", type=str, location="json")
# #
# #         super(Device, self).__init__()
# #
# #     # GET - Returns a single device object given a matching id
# #     def get(self, identifier):
# #         device = dal.get_device(identifier)
# #
# #         if not device:
# #             return {'message': 'Device not found', 'data': {}}, 404
# #
# #         return {"device": device}
# #
# #     # PUT - Given an id
# #     def put(self, identifier):
# #         args = self.reqparse.parse_args()
# #         updated_device = dal.put_device(identifier, args)
# #
# #         if not updated_device:
# #             return {'message': 'Device not found', 'data': {}}, 404
# #
# #         return {"updated device": updated_device}
# #
# #     # Delete - Given an id
# #     @staticmethod
# #     def delete(identifier):
# #         deleted = dal.delete_device(identifier)
# #
# #         if not deleted:
# #             return {'message': 'Device not found', 'data': {}}, 404
# #
# #         return deleted, 201
# #
# #
# # class DeviceInventory(Resource):
# #     def __init__(self):
# #         self.reqparse = reqparse.RequestParser()
# #         self.reqparse.add_argument(
# #             "id", type=str, required=True, help="Device id must be provided", location="json")
# #         self.reqparse.add_argument(
# #             "name", type=str, required=True, help="Device name must be provided", location="json")
# #         self.reqparse.add_argument(
# #             "location", type=str, required=True, help="Device location must be provided", location="json")
# #         self.reqparse.add_argument("status", type=str, required=True,
# #                                    help="Device status must be provided", location="json")
# #
# #         super(DeviceInventory, self).__init__()
# #
# #     @staticmethod
# #     def get():
# #         return dal.get()
# #
# #     def post(self):
# #         args = self.reqparse.parse_args()
# #         posted_device = dal.post(args)
# #         if not posted_device:
# #             return 404
# #         return {"device": posted_device}, 201
# #
# #
# # api.add_resource(DeviceInventory, "/items")
# # api.add_resource(Device, "/items/<string:identifier>")
# #
# # if __name__ == "__main__":
# #     app.run("0.0.0.0", port=5000, debug=True)
