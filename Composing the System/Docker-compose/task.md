## Composing our system
Now we have two flask apps: Invsys and Gateway. 
We want them both to be deployed, and we want Gateway to be able to send 
requests to Invsys using `invsys` instead of a specific IP.

**Docker-compose** is a tool that allows us to define the deployment of 
multiple containers, and has the added benefit of making each container 
targetable using the container name. All we need to do is create a `docker-compose.yaml` file
in our main project directory, which should look like this:

```text
version: '2'
services:
    gateway:
        build: gateway
        container_name: flask-app-gateway
        image: flask-app-gateway-img
        ports:
            - "5001:5001"
    invsys:
        build: invsys
        container_name: flask-app-invsys
        image: flask-app-invsys-img
```

We have defined two services. One for Gateway and one for Invsys. The key we use as the name 
of the service is the name used to target that service in the network. As we are naming our 
Invsys service as invsys, any requests from our application that target invsys will be routed 
to the correct ip for that service. We are using the `build` flag in each case, which means the 
tool will search for the gateway and invsys subdirectories and use their Dockerfiles to build 
the image. The `ports` flag is the same as the one used in the docker run command, it routes the 
external docker machine port to the internally exposed port of our containers. You'll notice 
that we haven't added a port mapping for invsys and this is because we want to force requests 
to go through the gateway. If you wanted to be able to target invsys directly too, you would 
just need to add ports: - `"5000:5000"`.

Add contents the `docker-compose.yaml` file and run the application. Test it with Postman like you did before.