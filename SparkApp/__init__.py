from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)   # Flask application module.
app.config['SECRET_KEY'] = '7b040a256ba53638fe34e81ccba6bb46'   # To encrypt data sent through forms.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///register/users.db'   # SQLite database.
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


from SparkApp.login import routes
from SparkApp.register import routes
from SparkApp.skills import routes
from SparkApp.tests import routes
from SparkApp.dashboard.student import routes
from SparkApp.dashboard.teacher import routes