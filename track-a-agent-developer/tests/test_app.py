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


def test_library_log_lines_stay_out_of_requests_log():
    import logging
    import app as app_module
    rec = lambda name: logging.LogRecord(name, logging.INFO, __file__, 1, 'HTTP Request: POST ...', None, None)
    assert not app_module.our_lines_only(rec('httpx2')) and not app_module.our_lines_only(rec('httpx'))
    assert app_module.our_lines_only(rec('root'))
    assert app_module.our_lines_only in app_module.log_file.filters
