from flask import Blueprint, Flask, url_for

core_bp = Blueprint('core', __name__)


@core_bp.route('/')
def hello_world():
    return 'Hello World'


@core_bp.route('/url')
def url():
    return url_for('core.url')

def init_app(app: Flask, url_prefix='/'):
    app.register_blueprint(core_bp, url_prefix=url_prefix)