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

