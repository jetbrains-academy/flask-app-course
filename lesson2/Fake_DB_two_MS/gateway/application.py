from flask import Flask, request, Response
import requests

app = Flask(__name__)


@app.route('/books', methods=['GET'])
@app.route('/books/<int:book_id>', methods=['GET'])
def get_resources(book_id=None):
    # Forward the request to the relevant endpoint in invsys
    if book_id:
        response = requests.get(f'http://invsys:5000/books/{book_id}')
    else:
        response = requests.get('http://invsys:5000/books')

    # Forward the response back to the client
    # We create a Response object by deconstructing our response from above
    return Response(response.content, response.status_code)


@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_resource(book_id):
    # Forward the delete request to the relevant endpoint in invsys
    response = requests.delete(f'http://invsys:5000/books/{book_id}')

    # Forward the response back to the client
    return Response(response.content, response.status_code)


@app.route('/books', methods=['POST'])
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_resource(book_id=None):
    # Get the payload from our incoming request
    payload = request.get_json(force=True)

    if request.method == 'POST':
        # Forward the payload to the relevant endpoint in invsys
        response = requests.post('http://invsys:5000/books', json=payload)
    else:
        response = requests.put(f'http://invsys:5000/books/{book_id}', json=payload)

    # Forward the response back to the client
    return Response(response.content, response.status_code)


if __name__ == "__main__":
    app.run("0.0.0.0", port=5001, debug=True)
