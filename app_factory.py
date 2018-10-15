from flask import Flask

import settings
from blueprints.core import bp as core_bp
from blueprints.users import bp as users_bp
from ext import postgres


def create_app(app_settings=None):
    if app_settings is None:
        app_settings = settings
    app = Flask(__name__)
    app.config.from_object(app_settings)
    postgres.init_app(app)
    core_bp.init_app(app)
    users_bp.init_app(app)
    return app
