Define function get_resources:
- Forward the request to the relevant endpoint in invsys
- Forward the response back to the client. Create a Response object by deconstructing our response from above


Looking at our `post_resource` function first, we want to take the payload from the incoming request and forward it to the instance of our
invsys. If we have deployed invsys on 127.0.0.1 then we could use:

```python
import requests

data = ... # from request
response = requests.post("http://127.0.0.1:5000/items", data)
```

However, by doing this, our application source code becomes coupled with how and where we deploy `invsys`.
So instead, we can post to `http://invsys:5000/items` and ensure that our network is set up to route `invys` to whichever ip it is hosted on.