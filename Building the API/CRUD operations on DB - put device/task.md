In this task, we are going to add another function to our DAL. 
It will be called from the API by the GET device endpoint.

1. Implement the `put_device` method in `dal`, which will take an `id` and `args` from the request. The method will update the device with the given `id` using the data from `args` 
if such an `id` is found, and then return the updated device. If no such `id` is found, it will return `None`.

2. Update the implementation of the PUT device endpoint in `api.py`.
