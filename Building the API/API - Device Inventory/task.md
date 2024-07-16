In this task, we're extending our API to include the `device_inventory` endpoint. Unlike the 
previous device endpoint, this endpoint handles operations on the entire database of 
devices rather than individual items. It is designed to handle operations that affect the 
entire device dataset, rather than individual entries. 

### Field validation
Custom validation logic is crucial to ensure the integrity and correctness of data 
sent to an API. In the context of our device inventory system, each device must 
have certain fields provided for the system to function properly: 
'id', 'name', 'location', and 'status'.

The `@validates_schema` decorator is used to define a method that is 
automatically invoked by Marshmallow to perform additional validations 
not covered by field-level validators. The method `validate_required_fields` 
should ensure that every required field is included in the POST request's JSON payload. 
If any of these fields are missing, a `ValidationError` is raised, resulting 
in an error response to the client with appropriate messaging.


### `device_inventory`
The `device_inventory` endpoint is responsible for managing operations on the entire 
datastore of devices. Here's what you need to implement:

1. GET Method: This method should return a JSON response containing all the devices in the datastore. 
The response should have an HTTP status code of 200. The JSON response body should have the following structure:
    ```json
    {"items": {
    "001": {"id": "001", "location": "hall", "name": "Light bulb", "status": "off"},
    "002": {"id": "002", "location": "bedroom", "name": "Humidity sensor", "status": "on"},
    "003": {"id": "003", "location": "bedroom", "name": "Humidifier", "status": "off"}
    }}
    ```

2. POST Method: When a JSON object representing a new device is sent via a POST request, 
this method should parse the object, validate it using the device_schema, and add a new key-value 
pair to the devices dictionary. If the device ID already exists in the database, 
return an appropriate error message `{ "message": "Device with this ID already exists" }` with a status code of 400. If the operation is successful, 
return a JSON response indicating that the device has been added (example below) with a status code 201.
   ```json
   {"Posted a device": {
   "id": "00111",
   "location": "bedroom",
   "name": "Humidity_sensor",
   "status": "off"} }
   ```

## Task

1. Define a method called `validate_required_fields` using the `@validates_schema` decorator within the `DeviceSchema` class.

2. Complete the implementation of the `device_inventory` endpoint for the methods GET and POST.

<div class="hint">

  In the method `validate_required_fields`, declare a list of `required_fields` containing the keys 'id', 'name', 'location', and 'status'.
Check if the current request method is POST (prevent unnecessary validation on other HTTP methods). If it is, iterate over the `required_fields` list.
For each field, check if the field is present in the `original_data` dictionary, which contains the data submitted by the user.
If any field is not present, raise a `ValidationError` with a custom message indicating which field is missing (`raise ValidationError(f'{field} is required.', field)`).

</div>

