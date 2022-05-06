No tests so far :(

Task: Add files necessary for running gateway app as a Docker container

<div class="hint">

```text
FROM python:3.8
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY . /app
WORKDIR /app
EXPOSE 5001
CMD [ "python", "application.py" ]
```
</div>

<div class="hint">See what you are importing in the application.py and add those packages to requirements.txt</div>