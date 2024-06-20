from flask import Flask, request, Response
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return 'Hello from Gateway!'


@app.route('/items', methods=['GET'])
@app.route('/items/<string:item_id>', methods=['GET'])
def get_devices(item_id=None):
    # Forward the request to the relevant endpoint in invsys
    if item_id:
        response = requests.get(f'http://0.0.0.0:5000/items/{item_id}')
    else:
        response = requests.get('http://0.0.0.0:5000/items')

    # Forward the response back to the client
    # We create a Response object by deconstructing our response from above
    return Response(response.content, response.status_code)


@app.route('/items/<string:item_id>', methods=['DELETE'])
def delete_device(item_id):
    # Forward the delete request to the relevant endpoint in invsys
    response = requests.delete(f'http://0.0.0.0:5000/items/{item_id}')

    # Forward the response back to the client
    return Response(response.content, response.status_code)


@app.route('/items', methods=['POST'])
def post_device():
    # Get the payload from our incoming request
    payload = request.get_json(force=True)
    response = requests.post('http://0.0.0.0:5000/items', json=payload)

    # Forward the response back to the client
    return Response(response.content, response.status_code)


@app.route('/items/<string:item_id>', methods=['PUT'])
def put_device(item_id):
    # Get the payload from our incoming request
    payload = request.get_json(force=True)
    response = requests.put(f'http://0.0.0.0:5000/items/{item_id}', json=payload)

    # Forward the response back to the client
    return Response(response.content, response.status_code)


if __name__ == "__main__":
    app.run("0.0.0.0", port=5001, debug=True)
