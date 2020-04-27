from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskapp.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail(app)

from flaskapp.users.routes import users
from flaskapp.posts.routes import posts
from flaskapp.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)