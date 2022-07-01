## DAL: DELETE device

In this task, we are going to add another function to our DAL. 
It will be called from the API by the `delete` method of the `Device` Resource.


Implement the `delete_device` method, that will delete a device from the database by its id and return a message in case of success. If the id wasn't found it should return `None`.