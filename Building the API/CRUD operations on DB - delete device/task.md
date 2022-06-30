## DAL: GET device, PUT device, DELETE device

In this task, we are going to add more functions to our DAL. 
These functions will be called from the API by `get`, `put` and `delete` methods of the `Device` Resource.

1. Implement the `get_device` method that will retrieve an item from the database by its identifier and return the device dictionary. It should return `None` if
the identifier wasn't found.
2. Implement the `put_device` method, which will take an id and args from the request, update the device with this id with the data from args, 
if such id is found, and then return an updated device. If not - return None.
3. Implement the `delete_device` method, that will delete a device from the database by its id and return a message in case of success. If the id wasn't found it should return `None`.