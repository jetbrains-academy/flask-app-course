## DAL: GET device

In this task, we are going to add another function to our DAL. 
It will be called from the API by the `get` method of the `Device` Resource.

Implement the `get_device` method that will retrieve an item from the database by its identifier and return the device dictionary. It should return `None` if
the identifier wasn't found.