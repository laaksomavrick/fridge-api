"""The configuration module"""
import os

#pylint: disable=too-few-public-methods


class Config():
    """The application configuration object"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URI') or 'postgresql://postgres:postgres@localhost:5432/fridge_dev'
    SQLALCHEMY_TRACK_MODIFICATIONS = False