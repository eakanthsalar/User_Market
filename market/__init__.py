from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'df81983fd08105e8974ac81e'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'  # when login is not done and when @login_required is used ...if not logged in then reroute to login page
login_manager.login_message_category = "info"
from market import routes

# app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'
