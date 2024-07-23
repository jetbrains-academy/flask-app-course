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
This would be totally okay if you wanted to deploy your applications locally (without Docker). However,
by doing this, our application source code becomes coupled with how and where we deploy `invsys`.
You can use `0.0.0.0` for local deployment if you like, but for checking this task, we ask 
you to replace it with `invsys`, so that your URL looks something like this: 
 `http://invsys:5000/items` (check out the URL in the `else` clause which is already completed). 
We will explain this in more detail in the next lesson. For now, you only need to know that
we use Docker under the hood to check these tasks, so `invsys` will be a designated name of a Docker Compose service and 
Docker will take care of names and routing.

<div class="hint">

  To create the right URL for getting a specific item, you only need to slightly modify the `get` URL that is already provided by adding the `item_id` to it.
</div>
