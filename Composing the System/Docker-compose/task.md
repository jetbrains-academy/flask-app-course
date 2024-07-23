Now we have two Flask apps: Invsys and Gateway. 
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

We have defined two services: one for Gateway and one for Invsys. The key we use as the name 
of the service is what we use to target that service in the network. Since we are naming our 
Invsys service as `invsys`, any requests from our application targeting `invsys` will be routed 
to the correct IP for that service. We are using the `build` flag in each case, which instructs the 
tool to search for the `gateway` and `invsys` subdirectories and use their Dockerfiles to build 
the image. 

The `ports` flag is the same as the one used in the `docker run` command: it routes the 
external Docker machine port to the internally exposed port of our containers. You'll notice 
that we haven't added a port mapping for `invsys`. This is intentional because we want to ensure that requests 
go through the gateway. If you want to allow direct targeting of `invsys` as well, you would 
just need to add `ports: - "5000:5000"` to the `invsys` service description.

<div class="hint" title="Secure port publishing">
By default, when you bind container ports to the host, they become available on all network interfaces.  
For experiments, this is not critical, but when deploying real applications, 
you should pay careful attention to which ports should be accessible from the outside world and which should not.

You can read more about how to properly publish ports [here](https://docs.docker.com/network/#published-ports).
</div>

Now, add the contents to the `docker-compose.yaml` file and run the application. Test it with HTTPie like you did before.
