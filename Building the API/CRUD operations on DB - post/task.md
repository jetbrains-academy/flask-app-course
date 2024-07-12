In this task, we are going to add a simple function to our DAL, which will handle adding data to the shelve database. 
This function will be called from the API when the `device_inventory` endpoint receives a `post` request.

1. Implement the `post` method, which will take `args` and add a new item (the `args` dictionary) to the database. The key for this item will be the value of the `id` from `args` (`args['id']`). Before doing that, the function should check 
if the provided `id` already exists in the storage, and if it does exist, return a message `{'error': 'Device with this ID already exists.'}` (this should be a dictionary, not a string).

2. In `api.py`, update the POST endpoint in the device inventory to work with `dal`.
