import pytest

from app_factory import create_app


@pytest.fixture
def app():
    app_obj = create_app()
    app_obj.testing = True
    with app_obj.test_request_context() as _:
        yield app_obj


@pytest.fixture
def client(app):
    client_obj = app.test_client()
    return client_obj
