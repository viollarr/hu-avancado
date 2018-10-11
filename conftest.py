import pytest

from app_factory import create_app


@pytest.fixture(scope='session')
def app():
    app_obj = create_app()
    app_obj.testing = True
    return app_obj


@pytest.fixture
def client(app):
    client_obj = app.test_client()
    return client_obj