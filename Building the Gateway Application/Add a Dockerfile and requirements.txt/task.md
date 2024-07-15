### Task 
Add the files necessary to run the gateway app as a Docker container.

<div class="hint">

```text
FROM python:3.10
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY . /app
WORKDIR /app
EXPOSE 5001
CMD [ "python", "application.py" ]
```
</div>

<div class="hint">Review the imports in `application.py` and add those packages to `requirements.txt`.</div>
