## Deploying in Cloud (Heroku)

[Heroku](https://www.heroku.com/) is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud,
and it makes the process really friendly for developers. Deploying your app on a service such as Heroku makes it publicly available on the web.

<i>This description of the process is far from being thorough, it is instead intended to give you a general idea of what needs to be done.</i>

To deploy your multiservice Flask application on Heroku, you can perform the following steps using the Terminal toolwindow in the IDE:

- [Create a Heroku account](https://signup.heroku.com/) if you don't have one already. Install the Heroku Command-Line Interface (CLI):
```shell
$ curl https://cli-assets.heroku.com/install.sh | sh
```

 **For each** of the microservices (`invsys` and `gateway`):
- `cd` into the app directory (`invsys` or `gateway`)
- Create and activate a Python virtual environment (here `venv`).
- Create a requirements.txt file listing the project’s dependencies (make sure to add all of them).

<details id="upd_routes">
    <summary>Update routes</summary>

Since each of the two microservices will now be deployed independently in the cloud, you need to adjust the routes in the `gateway` to target `invsys` appropriately.
For example, instead of 
```python
response = requests.get('http://invsys:5000/items')
```
you should have
```python
response = requests.get('http://flask-tutorial-invsys.herokuapp.com/items')
```
Here, the part `'flask-tutorial-invsys'` is the name of the app that you will specify yourself when creating the application in Heroku (see further).
</details>

- Initialize a Git repository for your project:
```shell
$ git init
```
- Add `venv` and `__pycache__` to .gitignore:
```shell
$ echo venv > .gitignore
$ echo __pycache__ >> .gitignore
```
- Add all the files you need to Git and make the initial commit:
```shell
$ git add app.py requirements.txt .gitignore 
$ git commit -m "Initial Commit"
```
- Now the project directory, for example `gateway`, should look like this:
```text
gateway/
│
├── .git/
│
├── venv/
│
├── .gitignore
├── app.py
├── dal.py
└── requirements.txt
```

- Log in to Heroku by running the following command:
```shell
$ heroku login
```
This opens a web page to complete the login process. After logging in, you can start using the Heroku CLI to manage your applications.

- Create a file named `Procfile` in the project’s root directory. This file tells Heroku how to run the app.
```shell
$ echo "web: gunicorn app:app" > Procfile
```
<details>

This file tells Heroku to serve your application using Gunicorn, a Python Web Server Gateway Interface (WSGI) HTTP server compatible with various web frameworks, including Flask.
The `web` label is used by Heroku to start the web server for your application. Heroku expects this label to be in your Procfile.
`app:app` specifies the module and the name of application that will be started by gunicorn. The module name and application name can be any other.
</details>

- Install Gunicorn and update the requirements.txt file using pip:
```shell
$ python3 -m pip install gunicorn
$ python3 -m pip freeze > requirements.txt
```
- Since you added and changed files, you need to commit them to Git.
```shell
$ git add Procfile requirements.txt
$ git commit -m "Added Heroku deployment files"
```
- Create the application in Heroku by running the following command:
```shell
$ heroku create flask-tutorial-invsys
```
Here, `'flask-tutorial-invsys'` is the name you specify yourself and the one you need to use in the routes as discussed <a href="#upd_routes">above</a>.

- Running the `heroku create` command initializes the Heroku application, creating a Git remote named `heroku`. You can now push your Git repository to this remote to trigger the build and deployment process:
```shell
$ git push heroku master
```
You will then see information about the building and deployment process. 
If something goes wrong, you can check heroku logs for errors to figure out what it was:
```shell
$ heroku logs --tail
```

After you've successfully deployed your microservices, you can test them using Postman just as we did before. 
Just remember to change the address in your requests: for example, you might need to use `https://flask-tutorial-gateway.herokuapp.com/items` instead of
`http://0.0.0.0:5001/items`.