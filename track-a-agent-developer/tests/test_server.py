import pytest

server = pytest.importorskip('server')


def test_check_availability():
    assert server.check_availability('2026-11-03') == ['09:00', '14:00']
    assert server.check_availability('2030-01-01') == []


def test_resource_and_prompt():
    assert '24 hours' in server.cancellation_policy()
    assert 'three bullet points' in server.intake_summary('notes')
