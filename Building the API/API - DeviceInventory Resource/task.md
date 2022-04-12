## API - Device Inventory Resource

Here we are going to define the `DeviceInventory` Class. It contains the routes dealing with operations on the entire database
instead of individual items.

The `init` method initializes the request parser. It parses the `request` JSON Object and validates it based on the arguments provided.
Note that by default, arguments are not required. Also, arguments supplied in the request that are not part of the RequestParser will be ignored.
Here we are going to make all arguments required (`"id"`, `"name"`, `"location"` and `"status"`) since we are going to need all of them in the 
`post` method to add a new item to the database.

The `get` method should simply return all the elements in the datastore of devices.

The `post` method takes a JSON Object, parses it, and adds a new key:value pair ("id": args) to the `devices` dictionary.

Add an endpoint for `DeviceInventory` Resource. This one is even more simple than the previous one,
the path does not contain any variables.
