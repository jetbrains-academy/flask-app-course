Our Flask API will provide an interface for managing a collection of devices stored within a database. 
It will facilitate the retrieval, updating, and deletion of devices using their unique identifiers.
We'll be building a simple API that performs basic CRUD operations on a datastore of devices. In this and the next task, we will
use a simple nested dictionary instead of a database. It can easily be swapped with a real database solution if needed. 

The `device` endpoint contains the HTTP routes for accessing, modifying, and deleting each individual device entity.

### Device schema

The `device_schema` defines a Marshmallow schema, which is utilized 
for validating the structure and content of the data sent in requests and 
responses. This schema ensures that the format of the device data adheres to 
specific requirements, such as mandatory fields and data types. This guarantees consistency 
and correctness in the information exchanged 
between the client and the server, enhancing the reliability of our API.

### Device methods

The operations are accessible via HTTP methods corresponding to standard CRUD operations:

`GET`: The GET request for a device by its identifier should check the device dictionary. 
If the device is present, return its data; if not, 
return a message `{'message': 'Device not found'}` and a response code `404`.

`PUT`: With a PUT request, the server expects an identifier and a set of data to update 
the corresponding device. The method should validate the provided data and update the 
device details if the identifier is valid. If the device is not found, it should
return a message `{'message': 'Device not found'}` and a response code `404`. If the data fails 
validation, it should return a `404` Not Found response code with the `ValidationError` message.

`DELETE`: On receiving a DELETE request with an identifier, the method should attempt to 
remove the corresponding device from the dictionary. If the device is not found, it should 
return a message `{'message': 'Device not found'}` and a response code `404`.

## Task

Complete the implementation of the `DeviceSchema`: add the remaining required fields.

Complete the implementation of the `device` endpoint.

1. For the `GET` request method, retrieve the device from the dictionary by its identifier.
2. For the `PUT` method, if the device is not found (there's no such identifier in our data), the function should
   return a message `{'message': 'Device not found'}` and a response code `404`.
3. For the `DELETE` method, delete the device with the identifier provided and return 
a message `{'message': 'Device deleted'}` and a response code `200`. If there's 
no such ID (key) in our data, return a message `{'message': 'Device not found'}` and a response code `404`. 
