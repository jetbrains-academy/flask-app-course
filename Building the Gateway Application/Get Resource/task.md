No working tests so far

## Get Resource

In this task we will define the `get_resource` function, which will:
- Forward the request to the relevant endpoint in invsys (depending on the url: if the item id is provided,
it needs to be added to the route, and the in the invsys it will result in calling the `get` method of the Device Resource)
- Forward the response back to the client. Create a Response object by deconstructing our response from above


Looking at our `get_resource` function at first we might want to take the incoming request and forward it to the instance of our
invsys. If we deployed invsys on 127.0.0.1 then we could use:

```python
import requests

data = ... # from request
response = requests.get("http://127.0.0.1:5000/items")
```

However, by doing this, our application source code becomes coupled with how and where we deploy `invsys`.
So instead, we can post to `http://invsys:5000/items` and ensure that our network is set up to route `invys` to whichever ip it is hosted on.