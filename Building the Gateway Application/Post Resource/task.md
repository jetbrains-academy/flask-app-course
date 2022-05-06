No working tests so far

## Post Resource

In this task we will define the `post_resource` function, which will:
- Get the payload from our incoming request.
- Forward the post request to the relevant endpoint in invsys. Do not forget the payload!
- Forward the response back to the client. Create a Response object by deconstructing `response`.

<div class="hint">

You can add payload with the argument `json=payload`.
</div>