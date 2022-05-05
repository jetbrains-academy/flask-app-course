from flask import Flask, request, Response
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return 'Hello from Gateway!'


if __name__ == "__main__":
    app.run("0.0.0.0", port=5001, debug=True)
