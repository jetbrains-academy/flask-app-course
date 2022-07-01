## DAL: POST

In this task, we are going to add a simple function to our DAL, which will be adding data to the shelve database. 
This function will be called from the API by the `post` method of the `DeviceInventory` Resource.

Implement the `post` method, which will take `args` and add a new item (the `args` dictionary) to the database, with its  key being the value of the `id` from `args` (`args['id']`).