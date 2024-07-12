Now, let's talk more about Dockerfile and requirements.txt.

### `requirements.txt`
As we discussed earlier, the list of packages needed for our application can be placed in a `requirements.txt` file,
which can then be committed to version control and shipped as part of the application.
Users can then install all the necessary packages with `pip install -r requirements.txt`. In our case, Docker will be installing the packages.
At this stage, you need to add `Flask`, `flask-restful`, and `marshmallow` to the file.

### `Dockerfile`
To deploy this microservice API to a Docker container, we first need to create a Dockerfile in the project directory.
A Dockerfile is essentially a set of instructions for building an image, which is a blueprint for our container to run from.
Let's go over this line by line:

```Dockerfile
FROM python:3.10
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY . /app
WORKDIR /app
EXPOSE 5000
CMD [ "python", "api.py" ]
```

- The line `FROM python:3.10` uses the Python 3.10 image from [Docker Hub](https://hub.docker.com/_/python) as our base image. This ensures we have Python and all its dependencies in the container.
- We `COPY requirements.txt /`, which makes the file available in our Docker image.
- Then, we install it using `RUN pip install -r /requirements.txt`.
- We then copy the rest of our source code into a subdirectory called `app` with `COPY . /app`.
- Using `WORKDIR /app` ensures that the next commands will be executed in that directory.
- The `EXPOSE 5000` instruction informs Docker that the container listens on port `5000` at runtime. We specified this port in `api.py`. The `EXPOSE` instruction doesn't publish the port to your host machine; it simply declares that this port is intended to be published.
- Finally, we state the command to run the application, which is `CMD [ "python", "api.py" ]`.

### Course testing system
Our course testing system will build the image using your `Dockerfile`, run the container, validate the solution with tests, and then remove the container. You will not need to do this manually. However, in the next couple of tasks, we will learn how to work with containers and test our application ourselves.

### Task
Fill in the contents of the `Dockerfile` and click the **Check** button to verify the task.