The next step will be creating an API gateway backend, which acts as a router for client requests.
This means our final application will consist of two backend components: the inventory
manager and the API gateway.

## Why could we need one?
- The gateway will allow us to present a single interface to access our microservices (in case we have several of those).
  From a technical perspective, it means the API client only needs to target a single
  host and single port instead of communicating with multiple services running on different ports and hosts.
  Firstly, it adds convenience.
- Another benefit of a gateway is that it can orchestrate the authentication and authorization of requests.
  Authentication is typically handled by an external system, but the gateway will
  communicate with that system to confirm that requests are authenticated before internally
  routing them to the correct microservices.
- The gateway can also handle authorization, which involves determining whether requests
  have permissions to access certain resources. In many cases, like the `invsys` system we
  developed above, we don't consider which client is consuming the service.
  By making our services client-agnostic, we allow them to focus on their specific purpose,
  making them more maintainable, discrete, and reusable. The gateway can
  then integrate middleware to determine which resources are accessible to which clients, potentially
  by integrating another microservice for handling client accounts and resources.

## What will ours do?
In this simple scenario, we want our gateway to just route requests to our `invsys` service.
Nothing else will be integrated, but by doing this, you will see how to consume one service from
another service. Once you can do it for one, you can do it for many.

## Gateway application structure

Inside our main project directory, we created a new directory called `gateway`. We will create another 
Flask application here, and it will be much simpler. Here, we will create a new Python environment
and install Flask again. We will also add a `requirements.txt` file and a Dockerfile later.
We created the `application.py` file in this new directory (it contains a dummy application at the moment). We expect our gateway application to receive requests from the API client, forward the payload or query strings to `invsys`,
and then forward the response from `invsys` back to the API client. All this will be happening in the `application.py` file; we do not need anything
else here.

To forward our requests, we will use the `requests` module, which can be installed using `pip install requests`.
Remember to add `requests` to `requirements.txt` later on.

