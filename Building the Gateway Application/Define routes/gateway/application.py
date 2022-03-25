from flask import Flask, request, Response
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return 'Hello from Gateway!'


@app.route('/items', methods=['GET'])
@app.route('/items/<string:item_id>', methods=['GET'])
def get_resources():
    pass


@app.route('/items/<string:item_id>', methods=['DELETE'])
def delete_resource():
    pass


@app.route('/items', methods=['POST'])
@app.route('/items/<string:item_id>', methods=['PUT'])
def update_resource():
    pass


if __name__ == "__main__":
    app.run("0.0.0.0", port=5001, debug=True)
