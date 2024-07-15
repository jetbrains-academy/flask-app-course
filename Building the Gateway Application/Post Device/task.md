In this task, we will define the `post_device` function, which will:
- Get the payload from our incoming request.
- Forward the POST request to the relevant endpoint in invsys. Do not forget the payload!
- Forward the response back to the client. Create a `Response` object from the received `response`.

<div class="hint">

You can add the payload using the argument `json=payload`.
</div>
