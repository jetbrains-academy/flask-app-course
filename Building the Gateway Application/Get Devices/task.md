## Get Devices

In this task, we will define the `get_devices` function, which will:
- Forward the request to the relevant endpoint in `invsys` (depending on the URL: if the item ID is provided,
it needs to be added to the route, which in `invsys` will result in calling the `get` endpoint in the function `device`)
- Forward the response back to the client. Create a `Response` object from the response received.


Looking at our `get_devices` function, at first, we might want to take the incoming request and forward it to the instance of our
`invsys`. If we deployed `invsys` on 127.0.0.1, then we could use:

```python
import requests

data = ... # from request
response = requests.get("http://0.0.0.0:5000/items/")
```
Let's keep it that way for this task, but let's also keep in mind that
by doing this, our application source code becomes coupled with how and where we deploy `invsys`.
Instead, we can post to `http://invsys:5000/items` and ensure that our network is set up to route `invsys` to whichever IP it is hosted on. 
We will come back to this later on.
