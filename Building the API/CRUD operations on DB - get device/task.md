In this task, we are going to add another function to our DAL. 
It will be called from the API by the GET device endpoint.

1. Implement the `get_device` method, which will retrieve an item from the database by its identifier and return the device dictionary. It should return `None` if
the identifier wasn't found.
2. Update the implementation of the GET device endpoint in `api.py`.
