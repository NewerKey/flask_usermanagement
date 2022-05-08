## Overview

This Flask application contains the basic user management functionality (register, login, logout)

Install the python packages specified in requirements.txt:

```sh
(venv) $ pip install -r requirements.txt
```

### Database Initialization

This Flask application needs a SQLite database to store data. The database should be initialized via the Flask shell:

```
(my_env4) $ flask shell
>>> from project import db
>>> db.drop_all()
>>> db.create_all()
>>> quit()
(my_env4) $
```

### Running the Flask Application

Run development server to serve the Flask application:

```sh
(my_env4) $ flask run
```

## Key Python Modules Used

- **Flask**: micro-framework for web application development which includes the following dependencies:
  - click: package for creating command-line interfaces (CLI)
  - itsdangerous: cryptographically sign data
  - Jinja2: templating engine
  - MarkupSafe: escapes characters so text is safe to use in HTML and XML
  - Werkzeug: set of utilities for creating a Python application that can talk to a WSGI server
- **pytest**: framework for testing Python projects
- **Flask-SQLAlchemy** - ORM (Object Relational Mapper) for Flask
- **Flask-Login** - support for user management (login/logout) in Flask
- **Flask-WTF** - simplifies forms in Flask
- **flake8** - static analysis tool

This application is written using Python 3.10.

## Testing

To run all the tests:

```sh
(my_env4) $ python -m pytest -v
```

To check the code coverage of the tests:

```sh
(my_env4) $ python -m pytest --cov-report term-missing --cov=project
```
