from flask import Blueprint, Flask

users_bp = Blueprint('users', __name__)


@users_bp.route('/new', methods=['POST'])
def new():
    return ''


def init_app(app: Flask, url_prefix='/users'):
    app.register_blueprint(users_bp, url_prefix=url_prefix)
