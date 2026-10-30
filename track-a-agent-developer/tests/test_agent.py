import copy, json
import pytest
import agent
from conftest import fake_client, make_msg, make_resp


@pytest.fixture(autouse=True)
def fresh_calendar():
    start = copy.deepcopy(agent.SLOTS)
    agent.BOOKINGS.clear()
    yield
    agent.SLOTS.clear(); agent.SLOTS.update(start); agent.BOOKINGS.clear()


def test_books_a_free_slot(monkeypatch):
    args = json.dumps({'name': 'Sam Lee', 'date': '2026-11-03', 'time': '14:00'})
    client, comp = fake_client([
        make_resp(make_msg(tool_calls=[('book_appointment', args)])),
        make_resp(make_msg('Booked: Sam Lee on 2026-11-03 at 14:00.')),
    ])
    monkeypatch.setattr(agent, 'client', client)
    assert '14:00' in agent.run('Book 14:00 on 2026-11-03 for Sam Lee')
    assert agent.BOOKINGS == [{'name': 'Sam Lee', 'date': '2026-11-03', 'time': '14:00'}]
    assert '14:00' not in agent.SLOTS['2026-11-03']


def test_bad_tool_arguments_do_not_crash(monkeypatch):
    client, comp = fake_client([
        make_resp(make_msg(tool_calls=[('book_appointment', '{not json')])),
        make_resp(make_msg(tool_calls=[('book_appointment', '["a list"]')])),
        make_resp(make_msg('Sorry, could you confirm the date?')),
    ])
    monkeypatch.setattr(agent, 'client', client)
    assert agent.run('book me') == 'Sorry, could you confirm the date?'
    tool_msgs = [m for m in comp.calls[-1]['messages'] if m.get('role') == 'tool']
    assert len(tool_msgs) == 2
    for m in tool_msgs:
        result = json.loads(m['content'])
        assert result['ok'] is False and result['reason'].startswith('bad arguments')


def test_unknown_tool_is_reported(monkeypatch):
    client, comp = fake_client([
        make_resp(make_msg(tool_calls=[('delete_everything', '{}')])),
        make_resp(make_msg('I cannot do that.')),
    ])
    monkeypatch.setattr(agent, 'client', client)
    agent.run('do something odd')
    tool_msg = [m for m in comp.calls[-1]['messages'] if m.get('role') == 'tool'][0]
    assert json.loads(tool_msg['content'])['reason'] == 'unknown tool'


def test_step_limit_hands_off(monkeypatch):
    loop = [make_resp(make_msg(tool_calls=[('check_availability', '{"date": "2026-11-03"}')]))
            for _ in range(agent.MAX_STEPS)]
    client, _ = fake_client(loop)
    monkeypatch.setattr(agent, 'client', client)
    assert agent.run('keep checking') == 'A staff member will contact you shortly.'


def test_cancel_appointment_lab_task():
    """A5 step 3. Skipped until you write cancel_appointment."""
    try:
        agent.book_appointment('Sam Lee', '2026-11-03', '09:00')
        result = agent.cancel_appointment('Sam Lee', '2026-11-03', '09:00')
    except NotImplementedError:
        pytest.skip('A5 step 3: cancel_appointment not written yet')
    assert '09:00' in agent.SLOTS['2026-11-03']
    assert 'cancel_appointment' in agent.REGISTRY
