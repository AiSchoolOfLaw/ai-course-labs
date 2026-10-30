import json, os
import pytest
from fastapi.testclient import TestClient


def test_health_and_masked_log(monkeypatch, tmp_path):
    import app as app_module
    monkeypatch.setattr(app_module, 'run', lambda text: 'Booked. We will text 202-555-0143.')
    client = TestClient(app_module.app)
    assert client.get('/health').json()['status'] == 'ok'
    r = client.post('/chat', json={'message': 'My email is ana@example.com'})
    body = r.json()
    assert body['reply'] == 'Booked. We will text [PHONE].'
    assert body['request_id']


def test_errors_return_safe_reply(monkeypatch):
    import app as app_module
    def boom(text):
        raise RuntimeError('provider down')
    monkeypatch.setattr(app_module, 'run', boom)
    r = TestClient(app_module.app).post('/chat', json={'message': 'hi'})
    assert 'staff member' in r.json()['reply']
