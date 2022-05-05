# Gateway Application

The next step will be an API gateway backend which is a sort of router of the client requests.
This means our final application will consist of two backend components, one being the inventory
manager, and the other being the api gateway.

## Why could we need one?
- The gateway will allow us to present a single interface to access our micro-services (in case we had several of those).
  From a technical perspective it means the API client only needs to target a single
  host and single port instead of communicating with multiple services running on different ports and hosts.
  So firstly it adds convenience.
- Another benefit of a gateway is that it can orchestrate the authentication and authorisation of requests.
  Authentication is typically handled by an external system, but then the gateway will
  communicate with that system to confirm requests are authenticated before internally
  routing them to the correct micro-services.
- The gateway can also handle authorisation, which is determining whether requests
  have permissions to access certain resources. In many cases, like the invsys system we
  developed above, we don't take into consideration which client is consuming the service.
  By making our services client-agnostic, we allow them to focus on their specific purpose
  which makes them more maintainable, more discrete, and more reusable. So the gateway could
  then integrate middleware that determines which resources are accessible to which clients, which
  itself might be done by integrating another micro-service for handling client accounts and resources.

## What will ours do?
In this simple scenario, we want our gateway to just route requests to our invsys service.
Nothing else will be integrated, but by doing this you will see how to consume one service from
another service, and when you can do it for one, you can do it for many.

## Gateway Application Structure

Inside our main project directory, we created a new directory called `gateway`. We will create another 
Flask application here, and it will be much simpler. Here we will create another fresh python environment
and install Flask again. requirements.txt and a Dockerfile will also be added again (later).
We created the `application.py` file in this new directory (it contains a dummy application at the moment). We expect our gateway application to receive requests from the API client, forward the payload or query strings to invsys,
then forward the response from invsys back to the API client. All this will be happening in the `application.py` file, we do not need anything
else here.

To forward our requests, we will use the `requests` module, which can install using `pip install requests`.
Remember to add `requests` to `requirements.txt` later on.

