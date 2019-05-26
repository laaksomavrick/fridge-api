"""The main application module."""

from flask import Flask, jsonify
from fridge import users
from fridge.config import Config
from fridge.db import DB


def create_app(config_object=Config):
    """The application factory function."""
    app = Flask(__name__)
    app.config.from_object(config_object)
    DB.init_app(app)
    app.register_blueprint(users.routes.blueprint)
    return app
