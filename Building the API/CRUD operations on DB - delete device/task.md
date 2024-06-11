## DAL: DELETE device

In this task, we are going to add another function to our DAL. 
It will be called from the API by the DELETE device endpoint.


1. Implement the `delete_device` method in dal, which will delete a device from the database by its id and return a message in case of success. 
If the id wasn't found it should return `None`. In case of success, it should return something like the message below and the `200` success code.

        
         {"message": "002 deleted"}


2. Update the implementation of the DELETE device endpoint in `api.py`



