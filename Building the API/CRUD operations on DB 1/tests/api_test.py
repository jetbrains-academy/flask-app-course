from flask import Flask
from flask_restful import Resource, Api, reqparse
import dal

# Initialize Flask
app = Flask(__name__)
api = Api(app)


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
        return dal.get()

    def post(self):
        args = self.reqparse.parse_args()
        posted_device = dal.post(args)
        if not posted_device:
            return 404
        return {"device": posted_device}, 201


api.add_resource(DeviceInventory, "/items")


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
