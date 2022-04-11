## API - Device Resource

The main building block provided by Flask-RESTful are resources. 
Resources are built on top of [Flask pluggable views](http://flask.pocoo.org/docs/views/), giving you easy access to 
multiple HTTP methods just by defining methods on your Resource Class.

We'll be building a simple API that goes over some basic CRUD operations on a datastore of devices. In this and the next task we are going
to use a simple nested dictionary instead of a database. It can easily be swapped in with a real database solution, should you need to. 

The Device Resource class contains the HTTP routes for accessing, modifying and deleting each individual device entity. 

In the `init` method of the class, you initialize the [request parser](https://flask-restful.readthedocs.io/en/latest/api.html#module-reqparse). It'll allow you easy access to any variable on 
the `flask.request` and also validates the response based on the arguments provided.

The `get` Method, takes an id and searches the dictionary for an element with such an id (key).
If it's absent, the method returns a message `{'message': 'Device not found', 'data': {}}` and a response code `404`.
If a match is found, it returns that device's dictionary. 

The `put` method is used to update the element with the specified id.
First it checks if the element with such an id is present in the dictionary, and if not, it returns
a message `{'message': 'Device not found', 'data': {}}` and a response code `404`.
It then parses all arguments from the provided request and stores the results as a Namespace `args`.
It loops through the parsed arguments (the same way you would parse a dictionary), and updates the fields in the corresponding device element.
It should also check for absent values in the request arguments and skip those (so that we so not update 
existing values with absent values).

The `delete` method first checks if the element with a given id is present in the dictionary, an if not, it returns
a message `{'message': 'Device not found', 'data': {}}` and a response code `404`.
It then simply deletes the element with this id from the devices dict.

