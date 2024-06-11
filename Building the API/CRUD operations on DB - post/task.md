## DAL: POST

In this task, we are going to add a simple function to our DAL, which will be adding data to the shelve database. 
This function will be called from the API when the `device_inventory` endpoint receives a `post` request.

1. Implement the `post` method, which will take `args` and add a new item (the `args` dictionary) to the database, with its key being the value of the `id` from `args` (`args['id']`). Before doing that, it should check 
if the provided id already exists in storage and if so, return a message `{'error': 'Device with this ID already exists.'}` (this is a dictionary, not a string).

2. In `api.py`, update the POST endpoint in the device inventory to work with dal.