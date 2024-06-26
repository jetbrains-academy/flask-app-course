from flask import Flask, jsonify
from marshmallow import Schema, fields

app = Flask(__name__)

# Define a simple Marshmallow Schema for our response
class HelloWorldSchema(Schema):
    hello = fields.Str()

# Instantiate the schema
hello_world_schema = HelloWorldSchema()

@app.route('/')
def get_hello():
    # Create a response object
    response = {"hello": "world"}
    # Use the schema to dump the response object to a formatted dictionary
    result = hello_world_schema.dump(response)
    return jsonify(result), 200

if __name__ == "__main__":
    app.run(debug=True)

