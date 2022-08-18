from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

# create an instance of SQLAlchemy (the ORM) with the Flask Application
db = SQLAlchemy(app)

# create an instance of Migrate which will be our migration engine and pass in the app and SQLAlchemy instance
migrate = Migrate(app, db, render_as_batch=True)
# create an instance of the LoginManager to handle authentication
login = LoginManager(app)
login.login_view = 'login' # tells the login manager which endpoint to redirect if someone is not logged in
login.login_message = 'You must be logged in to create a post.'
login.login_message_category = 'warning'

from . import routes, models

