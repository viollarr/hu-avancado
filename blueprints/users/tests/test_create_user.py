from flask import url_for


def test_status_code(client):
    resp = client.post(url_for('users.new'), data={'name': 'Renzo', 'age': '35'})
    assert resp.status_code == 200
