## DAL: PUT device

In this task, we are going to add another function to our DAL. 
It will be called from the API by the `put` method of the `Device` Resource.

Implement the `put_device` method, which will take an id and args from the request, update the device with this id with the data from args, 
if such id is found, and then return an updated device. If not - return `None`.