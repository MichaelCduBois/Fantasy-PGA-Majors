import os
from flask import Flask


def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    # Website Config
    # ToDo - Update SECRET_KEY
    app.config.from_mapping(

        SECRET_KEY='dev'

    )

    # Loads instance config, if it exists, when not testing
    if test_config is None:

        app.config.from_pyfile('config.py', silent=True)

    else:

        app.config.from_mapping(test_config)

    # Imports
    from . import index
    app.register_blueprint(index.bp)

    from . import leagues

    # Initializes the Applicaiton
    return app
