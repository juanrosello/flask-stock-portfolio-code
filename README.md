flask-stock-portfolio -> Test driven

Part1-ch1 - Setup

$ python3 --version
$ python3 -m venv venv
$ source venv/bin/activate  -> or $ . venv/bin/activate
(venv) $ pip install Flask
(venv) $ pip freeze

save the packages and version numbers being used:
(venv)$ pip freeze > requirements.txt  -> or $ pip freeze touch requirements.txt

specify where the Flask app is defined via FLASK_APP environment variable
(venv) $ export FLASK_APP=app.py

Configure the Flask Development Server to run in 'development' mode via FLASK_ENV environment variable.
(venv) $ export FLASK_ENV=development

Run the flask app:
$ flask run

To stop running the app:
CTRL+C

Navigate the app in your browser:
http://127.0.0.1:5000/

Turn back to you terminal after you view your site in the browser. You should see:
127.0.0.1 - - [30/Dec/2021 08:37:06] "GET / HTTP/1.1" 200 -

Structure (Exec in terminal):
(venv) $ tree -L 2

part1-ch4 - Routing

Create a about() -> function (view)
Default method=GET
define explicitly the methods as arguments passed in the function.

URL naming: 
1 with: /foo/
2 without: /foo

Variable Routing:
add variables to a URL, it get passed as arguments to the function.

Jinja templating engine:
1. Use static HTML template files to decouple the view from the HTML.
2. Separate the HTML structure from the content
3. se basic programming constructs -- variables, conditionals, and for loops -- directly in the HTML to manipulate the final rendered output

Create a folder with 3 HTML file.
Template rendering with render_template().

To allow different methods than GET, import requests too.

form validation
client-side validation
server-side validation

Install pydantic to perform server-side validation check:
(venv) pip install pydantic

add to the requirements file:
(venv) pip freeze > requirements.txt

Create a helper class(StockModel) at the top of app.py

Session in Flask:
Session object

Secret Key:
Since the session data is stored in a cryptographically-signed cookie, we need to specify a parameter in app.py called the secret key.
secrets module to generate a key.

Loading session data.
Redirects /add_stock to /stocks/

part1-ch8 - Testing with Pytest:
(venv) $ pip install pytest
(venv)$ pip freeze > requirements.txt

Run pytest:
(venv)$ python3 -m pytest

To see explicitly what happens with the tests:
(venv)$ python3 -m pytest -v

import pytest for the rasises excp ValueError
import pydantic for validationErrors

Run again:
(venv)$ python3 -m pytest -v

Functional Tests:
In order to create the proper environment for testing, Flask provides a test_client() helper.

Functional Tests (Part 2)
The key piece of functionality that we've implemented thus far is the ability to add a stock.

Steps:
Retrieve the form to add a stock (GET call to the '/add_stock' URL)
Submit the form to add a stock (POST call to the '/add_stock' URL)

To only run the functional tests, you can specify the folder like so:
(venv) $ python3 -m pytest tests/functional/

Static Files (images, CSS stylesheet, JS, HTML)
create a static folder in the project folder
create within the static folder a css and img folder. 

exec to see the structure:
$ tree -L 2

Favicon
A favicon is a very small icon that's frequently displayed in the tab of a webpage.

Inheritance and html code in css, and how to style the app.

part1-ch9 - Flash messages:
flash() func/method within the app.py

Loggin in Flask:
Add a log message to the index() view function in app.py.

Create a repository for the project:
1 - Create the repo in github.com

part2-ch12
Blueprints: divide your Flask project into separate components.

Stocks Blueprint:
handles stock portfolio management (add, delete, edit stocks in a portfolio)

Users Blueprint: 
handles user management (registration, login/logout, password reset)

Create the folder project:
create stocks and users folders
create a module file in each __init__.py

Exec this to see the routes:
$ flask routes

part2-ch13 Configuration Variables
FLASK_ENV - environment that the Flask app is running in (development or production)
DEBUG - enables debug mode
TESTING - enables testing mode
SECRET_KEY - used for securely signing the session cookie

in app.py bellow app = Flask:
app.config.from_pyfile('flask.cfg')
app.config.from_pyfile(os.environ['YOUR_APPLICATION_SETTINGS'])

Then
$ export YOUR_APPLICATION_SETTINGS=./config_development.py

part2-ch14, Factory Method Pattern:
Flask Application Factory
The initialization of a Flask app requires the following steps:

1 - Create the Flask application as an instance of the Flask class
2 - Set the configuration variables
3 - Register the blueprints in the project
4 - Configure the logger

Part2, ch13: Flask internals
States: 
Application Setup: app object - Handled by `create_app` function.
Steady-State: Request / Response processing - Handle by Blueprints.

Context:
1 Application context - keeps track of the application-level data (configuration variables, logger, etc.)
2 Request context - keeps track of the request-level data (URL, HTTP method, headers, request data, session, etc.)

Part2-ch14: Pytest Fixtures

The test fixture approach provides much greater flexibility than the classic Setup()/Teadown().
First, fixtures are defined as functions (that should have a descriptive names for their purpose).

In tests/conftest.py (where all fixtures should be defined), add a fixture to create the test client.

To really get a sense of when the test_client() fixture is run, 
pytest can provide a call structure of the fixtures and tests with the '--setup-show' argument:
(venv)$ python -m pytest --setup-show tests/functional/

Review context manager:
with statement context manager. 

Code/test coverage:
pytest-cov

(venv)$ pip install pytest-cov
(venv)$ pip freeze > requirements.txt

Tu run the coverage plugin:
(venv)$ python3 -m pytest --cov=project
=project is the Flask project structure.

Part2-ch17: Error Pages
abort()
error handlers
404, 405, 403 html templates

