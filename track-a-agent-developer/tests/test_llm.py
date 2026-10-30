import csv, json, os
import pytest
import llm
from conftest import fake_client, make_msg, make_resp


def test_ask_json_returns_data_and_logs_usage(monkeypatch):
    client, comp = fake_client([make_resp(make_msg(json.dumps({'category': 'billing', 'urgency': 'high'})))])
    monkeypatch.setattr(llm, 'client', client)
    data = llm.ask_json('Classify.', 'charged twice', ['category', 'urgency'])
    assert data == {'category': 'billing', 'urgency': 'high'}
    rows = list(csv.reader(open('usage.csv')))
    assert rows[-1][1:] == ['10', '5']


def test_ask_json_missing_keys_raises(monkeypatch):
    client, _ = fake_client([make_resp(make_msg(json.dumps({'category': 'billing'})))])
    monkeypatch.setattr(llm, 'client', client)
    with pytest.raises(ValueError, match='urgency'):
        llm.ask_json('Classify.', 'x', ['category', 'urgency'])


def test_chat_retries_then_succeeds(monkeypatch):
    calls = {'n': 0}
    ok = make_resp(make_msg('ok'))

    class Flaky:
        def create(self, **kw):
            calls['n'] += 1
            if calls['n'] < 3:
                raise RuntimeError('temporary')
            return ok

    import types
    monkeypatch.setattr(llm, 'client', types.SimpleNamespace(chat=types.SimpleNamespace(completions=Flaky())))
    monkeypatch.setattr(llm.time, 'sleep', lambda s: None)
    assert llm.chat([{'role': 'user', 'content': 'hi'}]) is ok
    assert calls['n'] == 3
