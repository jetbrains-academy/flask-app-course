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

        super(Device, self).__init__()

    # GET - Returns a single device object given a matching id
    @staticmethod
    def get(identifier):
        # device = dal.get_device(identifier)
        if identifier not in devices.keys():
            return {'message': 'Device not found', 'data': {}}, 404

        return {"device": devices[identifier]}


    # PUT - Given an id
    def put(self, identifier):
        args = self.reqparse.parse_args()
        # updated_device = dal.put_device(identifier, args)
        # Maybe this method should create a new device here if the id wasn't found, instead of returning a 404.
        # In this case, however, we need to make all args required.
        if identifier not in devices.keys():
            return {'message': 'Device not found', 'data': {}}, 404

        # Loop Through all the passed arguments.
        for k, v in args.items():
            # Check if the passed value is not null.
            if v is not None:
                # If not, set the element in the devices dict with the 'k' object to the value provided in the request.
                devices[identifier][k] = v

        # return {"updated device": updated_device}
        return {"updated device": devices[identifier]}, 200

    # Delete - Given an id
    @staticmethod
    def delete(identifier):
        # deleted = dal.delete_device(identifier)
        #
        # if not deleted:
        #     return {'message': 'Device not found', 'data': {}}, 404
        if identifier not in devices.keys():
            return {'message': 'Device not found', 'data': {}}, 404
        del devices[identifier]
        return {'message': f'{identifier} deleted'}, 200


api.add_resource(Device, "/items/<string:identifier>")

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
