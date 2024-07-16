CRUD stands for Create, Read/Retrieve, Update, and Delete, and these are the four basic operations that can be performed 
on persistence storage (database). HTTP methods can 
work as CRUD operations. The standard ones are as follows:

- POST: Creates a new device
- GET: Reads/Retrieves a device
- PUT: Updates an existing device
- DELETE: Deletes a device

In this task, we are going to add a simple function to our DAL, which will retrieve data from the shelve database. 
This function will be called from the API by the `device_inventory` function.

1. Implement the `get` method that will take all the data from the shelve and return a dictionary of devices (its structure should be the same as in the 
first task of this lesson). Remember that shelve objects can be accessed like a dictionary.
2. In `api.py`, import the data access layer and update the GET endpoint in the `device_inventory` to work with `dal`.
