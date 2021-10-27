# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
from flask import Flask

from freshfood import commands, restaurants, orders
from freshfood.extensions import  db, migrate, cors

from freshfood import commands
from freshfood.settings import ProdConfig
from freshfood.exceptions import InvalidUsage


def create_app(config_object=ProdConfig):
    app = Flask('fresh-food')
    app.url_map.strict_slashes = False
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    # register_shellcontext(app)
    register_commands(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    """Register Flask blueprints."""
    origins = app.config.get('CORS_ORIGIN_WHITELIST', '*')
    cors.init_app(restaurants.views.blueprint, origins=origins)
    cors.init_app(orders.views.blueprint, origins=origins)

    app.register_blueprint(restaurants.views.blueprint)
    app.register_blueprint(orders.views.blueprint)


def register_errorhandlers(app):
    def errorhandler(error):
        response = error.to_json()
        response.status_code = error.status_code
        return response

    app.errorhandler(InvalidUsage)(errorhandler)


def register_commands(app):
    """Register Click commands."""
    app.cli.add_command(commands.test)