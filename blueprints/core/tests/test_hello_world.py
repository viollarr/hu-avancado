import pytest


@pytest.fixture
def resp(client):
    resp_obj = client.get('/')
    return resp_obj


def test_status_code(resp):
    assert resp.status_code == 200


def test_content(resp):
    assert 'Hello World' in resp.get_data(as_text=True)
