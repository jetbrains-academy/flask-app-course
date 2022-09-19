## Modify the API

In this task, you will need to pair the API with the DAL. You should replace the mock api code we created 
in the first two steps (methods of the `Device` Resource and `DeviceInventory` Resource classes)
with calls of the corresponding functions from `dal.py`, so that the application actually works with the shelve datastore.

For example, instead of looking for a device like this:
```python
device = devices[identifier]
```

you would now need to do something like
```python
device = dal.get_device(identifier)
```
Then you need to adjust the remaining code accordingly. Do this for all the methods in the api.