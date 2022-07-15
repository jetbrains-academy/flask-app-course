## API - Device Inventory Resource

Here we are going to define the `DeviceInventory` Class. It contains the routes dealing with operations on the entire database
instead of individual items.

The `init` method initializes the request parser. It parses the `request` JSON Object and validates it based on the arguments provided.
Note that by default, arguments are not required. Also, arguments supplied in the request that are not part of the RequestParser will be ignored.
Here we are going to make all arguments required (`"id"`, `"name"`, `"location"` and `"status"`) since we are going to need all of them in the 
`post` method to add a new item to the database.

The `get` method should simply return a response (use `flask.make_response` to create it) all the elements in the datastore of devices in a form of a JSON object (build it using
`jsonify`), as well as code 200. The JSON part of the response should be something like this:

`{"items":{"001":{"id":"001","location":"hall","name":"Light bulb","status":"off"}, ... ... ,"003":{"id":"003","location":"bedroom","name":"Humidifier","status":"off"}}}`

<details>
    <summary>@staticmethod</summary>

[`@staticmethod`](https://docs.python.org/3/library/functions.html#staticmethod) is a built-in [decorator](https://docs.python.org/3/glossary.html#term-decorator) that defines a static method - method that doesn't
receive an implicit first argument (`self`) whether it is called by an instance of a class or by the class itself.
</details>

The `post` method takes a JSON Object, parses it, and adds a new key:value pair ("id": args) to the `devices` dictionary.

Add an endpoint for `DeviceInventory` Resource. This one is even more simple than the previous one,
the path does not contain any variables.
