from flask import Flask, request, Response
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return 'Hello from Gateway!'


@app.route('/items', methods=['GET'])
@app.route('/items/<string:item_id>', methods=['GET'])
def get_resources(item_id=None):
    # Forward the request to the relevant endpoint in invsys
    if item_id:
        response = requests.get(f'http://invsys:5000/items/{item_id}')
    else:
        response = requests.get('http://invsys:5000/items')

    # Forward the response back to the client
    # We create a Response object by deconstructing our response from above
    return Response(response.content, response.status_code)


@app.route('/items/<string:item_id>', methods=['DELETE'])
def delete_resource():
    # Forward the delete request to the relevant endpoint in invsys
    response = requests.delete(f'http://invsys:5000/items/{item_id}')

    # Forward the response back to the client
    return Response(response.content, response.status_code)


@app.route('/items', methods=['POST'])
@app.route('/items/<string:item_id>', methods=['PUT'])
def update_resource():
    pass


if __name__ == "__main__":
    app.run("0.0.0.0", port=5001, debug=True)
