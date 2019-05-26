"""The main application package."""

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import users

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(users.routes.blueprint)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# circular dependency
from app import routes, models