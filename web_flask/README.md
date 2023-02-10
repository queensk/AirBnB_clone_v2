# 0x04. AirBnB clone - Web framework

## What is a Web Framework

A web framework is a software framework designed to support the development of web applications. It provides a set of tools, libraries, and patterns that simplify the process of building web applications and help to standardize the development process. Web frameworks are designed to handle common web development tasks, such as routing, handling HTTP requests, rendering templates, and working with databases, so that developers can focus on writing application-specific code.

How to build a web framework with Flask
Flask is a lightweight Python web framework that provides a simple and easy-to-use interface for building web applications. To build a web application with Flask, you'll need to install Flask and its dependencies, create a new Flask application, and define the routes for your application.

Here's a simple example of how to build a web application with Flask:

```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()
```

## How to define routes in Flask

In Flask, routes are defined using the @app.route decorator. The @app.route decorator takes a URL pattern as an argument and maps it to a function that will handle the incoming request. For example:

```
@app.route('/')
def index():
    return "Hello, World!"

@app.route('/hello/<name>')
def hello_name(name):
    return "Hello, {}!".format(name)
```

## What is a route

A route is a mapping between a URL pattern and a function that will handle incoming requests for that URL. In Flask, routes are defined using the @app.route decorator. When a user visits a URL, Flask matches the URL against the defined routes and calls the associated function to generate the response.

How to handle variables in a route
Variables can be included in the URL pattern of a route, and the values of these variables can be passed to the function that handles the incoming request. In Flask, variables are specified in the URL pattern using angle brackets (< and >). For example:

```
@app.route('/hello/<name>')
def hello_name(name):
    return "Hello, {}!".format(name)
```

## What is a template

A template is a blueprint or blueprint-like document that defines the structure and content of a web page. Templates are typically written in a templating language, such as Jinja2 in Flask, which allows for dynamic content to be inserted into the template. In Flask, templates are stored in a separate directory and can be rendered by passing data to the template and calling the render_template function.

## How to create a HTML response in Flask by using a template

In Flask, you can use templates to generate HTML responses. To use a template, you'll need to create the template file in a templates directory and define the template using a templating language, such as Jinja2. You can then use the render_template function to render the template and return the generated HTML as the response.

Here's an example of how to create a HTML response using a template in Flask:

```
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
```

## How to create a dynamic template (loops, conditions…)

To create a dynamic template, you can use the features of the templating language, such as loops and conditions, to generate dynamic content based on the data passed to the template. In Flask, you can use the Jinja2 templating language to create dynamic templates.

Here's an example of how to use loops and conditions in a Jinja2 template:

```
<ul>
{% for item in items %}
  {% if item.published %}
    <li>{{ item.title }}</li>
  {% endif %}
{% endfor %}
</ul>
```

## How to display in HTML data from a MySQL database

To display data from a MySQL database in a Flask application, you'll need to connect to the database and retrieve the data. You can use a library such as mysql-connector-python to connect to a MySQL database and retrieve the data. Once you have the data, you can pass it to the template and use the templating language to display the data in HTML.

Here's an example of how to retrieve data from a MySQL database and display it in HTML using Flask and Jinja2:

```
import mysql.connector
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    conn = mysql.connector.connect(user='user', password='password', host='host', database='database')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM table')
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', data=data)
```
