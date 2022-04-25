# DTLAB-API
This is an activity for DTLAB class about chapters 5-6 of DEVASC course.

## Description

Using [Flask](https://flask.palletsprojects.com/en/2.1.x/), students will work together to create a simple REST service to manage network devices. Different groups will cover different functionalities, as shown in the instructions.
There will be 3 core functionalities:
* Managing switches: user will have a CRUD interface for switches;
* Managing routers: user will have a CRUD interface for routers;
* Configuring devices: user will configure devices by updating switches and devices model;

Each group will submit a pull request on a branch named by group name.

## Instructions

### Part 1 - Create a development environment (10 minutes)

The application uses Flask as Web framework and [Postgres](https://www.postgresql.org/docs/) to store data. First of all, install project dependencies after creating a new virtual env using the following command:

```
pip install -r requirements.txt
```

Start a Postgres instance using Docker. The application loads database configuration from `.env` file. In order to start Postgres, look at the official documentation on [Docker Hub](https://hub.docker.com/_/postgres).

*WARNING* database configuration must match with the one provided in `.env`. Do not change variable names but only values (*after = sign*).

Execute the app with the command:

```
flask run
```

*HINT*: to enable hot reload when developing, set `FLASK_ENV` variable to `development`. For example, on Linux:

```
FLASK_ENV=development flask run
```

Check if everything is working using the following command:

```
curl http://localhost:5000/test
```

or just open the browser at the `/test` endpoint.
### Part 2 - Implement the assigned function (40 minutes)

A CRUD interface is a set of standard operations that permits to Create, Read, Update and Delete data and represents the fundamental of a REST API.

Depending on what you have been assigned, open the correct file and create the requested endpoint. In each file, there is a variable called `~_blueprint` which holds the router. Looking at the example routes and the documentation create the requested endpoint, minding that alla routes are prefixed with a prefix specifified in `app.py`. For example, switches endpoint is mounted at `/devices/switches` which means that all requests that are going to hit the switches endpoint must match with this prefix. For example a `GET` request may look like:

```
curl http://localhost:5000/devices/switches
```

So everything added to the path will be appended to the prefix, for example a `/all` endpoint will become:

```
curl http://localhost:5000/devices/switches/all
```

To test what you have done, use **Postman** as you learned in chapter 4.

#### Handler structure

Generally, an HTTP handler follows a standard structure:
* get request data;
* validate request data;
* perform requested operations;
* return a response;

#### Accessing the database

Database access is implemented using [SQL Alchemy](https://docs.sqlalchemy.org/en/14/orm/quickstart.html). Usage is simplified with *DB* class provided in `db.py` file. To get a valid connection to the database you will need to use `DB.getSession()` static method in the class.
Look at the documentation linked above and example below to learn how to perform simple queries. 
Feel free to change everything as you want!

For example, to store a switch:

```python
from db import DB, Switch

with DB.getSession() as session:
    switch = Switch(
        hostname: 'switch1'
    )
    session.add(switch)
    session.commit()
```

To query an object:

```python
from sqlalchemy import select
from db import DB, Switch


with DB.getSession()as session:
    stmt = select(Switch).where(Switch.hostname=='switch1')
    switch = session.scalars(stmt).one()
```

### Part 3 - Commit your changes (10 minutes)

After finishing the implementation, it's time to commit new changes and submit a pull request to the central repository!

You can learn on how to submit a pull request [here](https://opensource.com/article/19/7/create-pull-request-github).

## Bonus activities

Complete these activities once you have finished previous steps. Following activities can be completed at home individually.

### Bonus 1 - Prepare the application for a Docker deploy

Use what you have learned in chapter 6 to write a Dockerfile and deploy the application using the container model.

### Bonus 2 - Protect the endpoint with authentication

Use what you have learned in chapter 4 and look at the [documentation](https://pythonhosted.org/Flask-JWT/).

### Bonus 3 - Create a CI/CD pipeline using Jenkins

Based on what you have done in the lab 6.3.6 to build a pipeline with Jenkins.