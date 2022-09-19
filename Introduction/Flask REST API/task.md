## Flask REST API

Flask is a micro web framework written in Python. The “micro” in microframework means 
Flask aims to keep the core simple but extensible. Flask won’t make many decisions for you, such as what database to use.
By default, Flask does not include a database abstraction layer, form validation or anything else where different libraries 
already exist that can handle that. Instead, Flask supports extensions to add such functionality to your application as 
if it was implemented in Flask itself.

Flask may be “micro”, but it’s ready for production use on a variety of needs.
Applications that use the Flask framework include Pinterest and LinkedIn.

### API

An application programming interface (API) is a connection between computers or between computer programs. It is a type of software interface, offering a service to other pieces of software. A document or standard that describes how to build or use such a connection or interface is called an API specification. A computer system that meets this standard is said to implement or expose an API. The term API may refer either to the specification or to the implementation.

In contrast to a user interface, which connects a computer to a person, an application programming interface connects computers or pieces of software to each other.

### REST API

REpresentational State Transfer (REST) is an architectural style that defines a set of constraints for creating web services. 
REST API is a way of accessing web services in a simple and flexible way without any processing.
REST technology is generally preferred to the Simple Object Access Protocol (SOAP) technology because REST uses less bandwidth, 
while its simplicity and flexibility makes it more suitable for internet usage. REST API is used to fetch or send some information to a web service, and the communication uses only HTTP requests.

### Flask-RESTful

Flask-RESTful is an extension for Flask that adds support for quickly building REST APIs. It is a lightweight abstraction that works with your 
existing ORM/libraries. Flask-RESTful encourages best practices with minimal setup. If you are familiar with Flask, Flask-RESTful should be easy to pick up.
A minimal Flask-RESTful API is shown in the code editor. Note that we’ve enabled [Flask debugging mode](http://flask.pocoo.org/docs/quickstart/#debug-mode) to provide code reloading and better error messages.
Debug mode should never be used in a production environment!

You can test the API using `curl` or by going to http://127.0.0.1:5000/ in your web browser. To terminate the application, press the stop ![img](run_stop.svg) button in the 
[run tool window](https://www.jetbrains.com/help/idea/run-tool-window.html). Do not forget to terminate your app before running a new one or before going to a next task.

<style>
img {
  display: inline !important;
}
</style>
