flask-stock-portfolio -> Test driven

Part 1:

SETUP:

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

ROUTING:

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

Pytest:

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

Flash messages:
flash() func/method within the app.py

Loggin in Flask:
Add a log message to the index() view function in app.py.

Create a repository for the project:
1 - Create the repo in github.com
