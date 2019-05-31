from flask import Flask
from fridge import user, sticky
from fridge.config import Config
from fridge.extensions import db, migrate
from fridge.exceptions import ApiError


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(user.routes.blueprint)
    app.register_blueprint(sticky.routes.blueprint)

    register_errorhandlers(app)

    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, 'User': user.models.User,
                'Sticky': sticky.models.Sticky}

    return app


def register_errorhandlers(app):

    def errorhandler(error):
        response = error.to_json()
        response.status_code = error.status_code
        return response

    app.errorhandler(ApiError)(errorhandler)
