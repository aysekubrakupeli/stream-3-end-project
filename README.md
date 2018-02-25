# Carebook
**Ecommerce & Blog Web Application with User Authentication and Stripe Payments**

This is the final Bootcamp Stream 3 project. It is a **fictional** social media site built with Python's *Django* framework with ecommerce functionality (Stripe) - no template was used.

## Live Demo

**Follow this link to view deployed version of the web app https://aysekubrakupeli-carebook.herokuapp.com/**

## Built with 
1. Django framework
2. Python
2. HTML
3. CSS
4. Bootstrap
5. SQLite database

## URL's

urls.py at the project level (Carebook) gives the url patterns routes to views, either directly Or for the Apps that have their own urls, via the 'include' function:

 `from accounts import urls as accounts_urls`

 `urlpatterns = [url(r'^accounts/', include(accounts_urls))]`

## Views

Views called via URLs are Python functions that perform the different actions required to make the Website function e.g. render a template, log someone in, log them out etc.

## Templates

The base.html page in the top-level templates folder is the base template used for all pages and includes all the links CSS/Bootstrap/Javascript etc. and the fully responsive navbar and footer that appears on all pages of the Website. 
It also contains:
```
{% block content %}
{% endblock content %}
```
Which allows other templates to be inserted in to that section (between the navbar & footer). Linking the base.html to templates within Apps:
```
{% extends 'base.html' %}

{% block content %}

All code for the app goes in here & will appear between the navbar & footer from base.html

{% endblock content %}
```

## Apps

#### Accounts

The Accounts App is used for full user authentication. When users first visit the website they have two options under 'My Account' - Register if they have no account or Log In if they do. Once Registered/Logged in they can view their own profile that will display their username and email address they used to register with. The two options under 'My Account will then change to Profile or Log Out. It is possible for users to Subscribe to a monthly magazine - once clicked the subscribe function is called within the views.py in the Accounts App which connects with Stripe payments and if the card details are entered correctly into the form it will take a monthly payment from the user.

#### Blog

This App displays the Posts that have been added either via Django's admin panel or personal profiles on the front end of the site.

#### Checkout

Checkout app gives the option for users to donate money to each other. With the amounts they donate they earn Ego points. With these ego points they are able to go higher up the ranks of the social lader. 

The home page also updates automatically when a new post is added - showing only the 3 newest posts.

## Deployment / Hosting

This Project was deployed and is hosted on Heroku with automatic deploys from GitHub

## Databases / Static Files

When running locally, SQLite database was used & static and media files were stored locally.
When deploying, Heroku Postgres was used as the server database & an Amazon S3 bucket was set up to host all the static files. settings.py file was amended for the database & static files to point to the online resources.


## Installation

Follow the below instructions to clone this project for Mac (commands will be slightly different for Windows)

1. Go to folder you want to put the cloned project in your terminal & type:
    `$ git clone https://github.com/aysekubrakupeli/stream-3-end-project`
2. Create & Activate a new Virtual Environment in terminal:
    Create: `$ python3 -m venv ~/virtualenvs/name_of_environment`
    Activate: `$ source ~/virtualenvs/name_of_environment/bin/activate`
3. Install the project dependancies:
    `$ pip install -r requirements.txt`
4. Create env.sh file at the top level (this will contain all sensitive information)
    **MAKE SURE IT IS IN THE .gitignore FILE**
5. After the download you'll have to create a env.sh file and edit the settings of the project. If you want to work on the project or make adjustments for yourself do contact me through my social media. 

## Running the tests

Automated tests can be viewed in the tests.py file within the separate Apps. 
To run the tests, in your terminal navigate to the folder with your project in, activate your virtual environment and type:

`$ python manage.py test <app name>`

* `$ python manage.py test accounts` - These will all PASS
    tests.py n the Accounts App:
    1. Tests that the UserRegistrationForm validates properly when the correct information is supplied
    2. Tests that the form fails when one of the passwords has not been entered
    3. Tests that the form fails when the passwords to not match

* `$ python manage.py test cart` - This will PASS
    tests.py in the Cart App:
    1. Tests that the url for '/cart/' resolves to the 'cart' function in views.py

* `$ python manage.py test contact` - These will both PASS
    tests.py in the Contact App:
    1. Tests that the url for '/contact/' resolves to the 'contact' function in views.py
    2. Tests that the view returns the correct status code 






