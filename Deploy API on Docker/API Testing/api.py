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
        devices_dict = dal.get()
        return jsonify({"items": devices_dict}), 200

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

