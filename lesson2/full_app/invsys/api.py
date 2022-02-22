from flask import Flask
from flask_restful import Resource, Api, reqparse
import dal

# Initialize Flask
app = Flask(__name__)
api = Api(app)


# Resource: Individual Device Routes
class Device(Resource):
    def __init__(self):
        # Initialize The Flask Request Parser and add arguments as in an expected request
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("id", type=str, location="json")
        self.reqparse.add_argument("name", type=str, location="json")
        self.reqparse.add_argument("device_type", type=str, location="json")
        self.reqparse.add_argument("controller_gateway", type=int, location="json")

        super(Device, self).__init__()

    # GET - Returns a single device object given a matching id
    def get(self, identifier):
        device = dal.get_device(identifier)

        if not device:
            return {'message': 'Device not found', 'data': {}}, 404

        return {"device": device}

    # PUT - Given an id
    def put(self, identifier):
        args = self.reqparse.parse_args()
        updated_device = dal.put_device(identifier, args)

        if not updated_device:
            return {'message': 'Device not found', 'data': {}}, 404

        return {"updated device": updated_device}

    # Delete - Given an id
    @staticmethod
    def delete(identifier):
        deleted = dal.delete_device(identifier)

        if not deleted:
            return {'message': 'Device not found', 'data': {}}, 404

        return deleted, 201


class DeviceInventory(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            "id", type=str, required=True, help="Device id must be provided", location="json")
        self.reqparse.add_argument(
            "name", type=str, required=True, help="Device name must be provided", location="json")
        self.reqparse.add_argument(
            "device_type", type=str, required=True, help="Device type must be provided", location="json")
        self.reqparse.add_argument("controller_gateway", type=int, required=True,
                                   help="Controller_gateway must be provided", location="json")

        super(DeviceInventory, self).__init__()

    @staticmethod
    def get():
        return dal.get()

    def post(self):
        args = self.reqparse.parse_args()
        posted_device = dal.post(args)
        if not posted_device:
            return 404
        return {"device": posted_device}, 201


api.add_resource(DeviceInventory, "/items")
api.add_resource(Device, "/items/<string:identifier>")

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
