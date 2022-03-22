FROM python:3.8
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY . /app
WORKDIR /app
EXPOSE 5001
CMD [ "python", "application.py" ]
