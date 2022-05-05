## Put Resource

In this task we will define the `put_resource` function, which will:
- Get the payload from our incoming request.
- Forward the post request to the relevant endpoint in invsys. Do not forget the payload!
- Forward the response back to the client. Create a Response object by deconstructing `response`.

<div class="hint">

This is similar to the previous one, only need to add `item_id` to the route.
</div>