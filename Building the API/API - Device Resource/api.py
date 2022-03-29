from flask import Flask
from flask_restful import Resource, Api, reqparse

# Initialize Flask
app = Flask(__name__)
api = Api(app)

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
    def get(self, identifier):
        # device = dal.get_device(identifier)
        device = next((item for item in devices if item['id'] == identifier), None)

        if not device:
            return {'message': 'Device not found', 'data': {}}, 404

        return {"device": device}

    # PUT - Given an id
    def put(self, identifier):
        args = self.reqparse.parse_args()
        # updated_device = dal.put_device(identifier, args)
        for device in devices:
            if device.get('id', 0) == identifier:
                for k, v in args.items():
                    if v is not None:
                        device[k] = v
                break
        else:
            # if not updated_device:
            return {'message': 'Device not found', 'data': {}}, 404

        # return {"updated device": updated_device}
        return {"updated device": next((item for item in devices if item['id'] == identifier), None)}

    # Delete - Given an id
    @staticmethod
    def delete(identifier):
        # deleted = dal.delete_device(identifier)
        #
        # if not deleted:
        #     return {'message': 'Device not found', 'data': {}}, 404

        for i in range(len(devices)):
            if devices[i]['id'] == identifier:
                del devices[i]
                break
        else:
            return {'message': 'Device not found', 'data': {}}, 404

        return {'message': f'{identifier} deleted'}, 201
