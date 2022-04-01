### What are Microservices?

Microservices are an architectural and organizational approach to software development where software is composed of small independent services.
In monolithic architectures, all processes are tightly coupled and run as a single service.
Adding or improving features of a monolithic application becomes more complex as the code base grows. 
This limits scalability and makes it difficult to implement new ideas. 

With a microservice architecture, an application is built as independent components, each performing a single function and
communicating with each other over lightweight APIs. 
Each component service in a microservice architecture can be developed, deployed, operated, and scaled without affecting the functioning of other services. 

### What will we build?

What we intend to make is a backend application consisting of multiple micro-services.
We'll be building a simple API that performs some basic CRUD operations on a database of smart home devices. For simplicity, we are going
to be using a Python `shelf` object instead of a real database solution.
The additional step will be an API gateway backend which is a sort of router and authoriser of the client requests.
This means our application will consist of two backend components, one being the inventory manager, and the other being the API gateway.
The application will expose a RESTful interface.