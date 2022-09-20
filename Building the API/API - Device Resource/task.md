## API - Device Resource

The main building block provided by Flask-RESTful are resources. 
Resources are built on top of [Flask pluggable views](http://flask.pocoo.org/docs/views/), giving you easy access to 
multiple HTTP methods just by defining methods on your Resource Class.

We'll be building a simple API that goes over some basic CRUD operations on a datastore of devices. In this and the next task we are going
to use a simple nested dictionary instead of a database. It can easily be swapped in with a real database solution, should you need to. 

The Device Resource class contains the HTTP routes for accessing, modifying and deleting each individual device entity. 

### Device Resource methods

In the `init` method of the class, you initialize the [request parser](https://flask-restful.readthedocs.io/en/latest/api.html#module-reqparse). 
It'll allow you easy access to any variable on 
the `flask.request` and also validates the response based on the arguments provided.
Request parser looks for arguments of a specified type (in our case, `str`) in the `flask.Request.values` dict.
By default, arguments are not required. 

The `get` method, takes an id and searches the dictionary for an element with such an id (key).
If it's absent, the method returns a message `{'message': 'Device not found', 'data': {}}` and a response code `404`.
If a match is found, it returns that device's dictionary.

The `put` method is used to update the element with the specified id.
First it checks if the element with such an id is present in the dictionary, and if not, it returns
a message `{'message': 'Device not found', 'data': {}}` and a response code `404`.
It then parses all arguments from the provided request and stores the results as a Namespace `args`.
It loops through the parsed arguments (the same way you would parse a dictionary), 
and updates the fields in the corresponding device element.
It should also check for absent values in the request arguments and skip those (so that we so not update 
existing values with absent values).

The `delete` method checks if the element with a given id is in the dictionary, and if not, it returns
a message `{'message': 'Device not found', 'data': {}}` and a response code `404`.
If the element is found, it simply deletes the element with this id from the `devices` dict.

### Endpoints

The line

```python
api.add_resource(Device, "/items/<string:identifier>")
```

attaches the `Device` class to an [endpoint](https://flask-restful.readthedocs.io/en/latest/quickstart.html?highlight=endpoints#endpoints).
You can pass multiple URLs to the `add_resource()` method on the `Api` object. Each one will be routed to your `Resource`.
You can also match parts of the path as variables to your `Device` methods.

## Task

Complete the implementation of the `Device` Resource.

1. In the `init` method, add the missing arguments.
2. In the `get` method, after trying to get a device from the dictionary by its id, return the `not_found_response` in case there's no such id.
3. In the `put` method, if there's no such id (key) in our data, return the `not_found_response`. Then loop through all the passed arguments and their values (it's like a dictionary).
For each argument value, check if it is not empty (None). If not, update the corresponding argument value of the
corresponding device with the value provided in the request.
4. In the `delete` method, delete the device with the identifier provided. If there's no such id (key) in our data, return the `not_found_response`. 
