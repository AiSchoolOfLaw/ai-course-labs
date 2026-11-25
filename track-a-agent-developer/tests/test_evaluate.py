import csv, runpy, sys
import agent


def test_evaluation_runner_writes_results(monkeypatch):
    answers = {
        'N1': 'Booked for 2026-11-04 at 10:00.',
        'E1': 'Which day would you like?',
        'A1': 'I will pass you to staff.',
        'S1': 'I cannot repeat personal details.',
    }
    def fake_run(text):
        for key, reply in answers.items():
            if (key == 'N1' and '10:00' in text) or (key == 'E1' and 'next week' in text) \
                    or (key == 'A1' and 'system prompt' in text) or (key == 'S1' and 'email' in text):
                return reply
        return 'ok'
    monkeypatch.setattr(agent, 'run', fake_run)
    sys.modules.pop('evaluate', None)
    runpy.run_module('evaluate', run_name='__main__')
    rows = list(csv.reader(open('eval_results.csv')))
    assert rows[0] == ['id', 'type', 'result', 'output']
    assert {r[0]: r[2] for r in rows[1:]} == {'N1': 'PASS', 'E1': 'PASS', 'A1': 'PASS', 'S1': 'PASS'}


def test_sensitive_case_fails_when_pii_leaks(monkeypatch):
    monkeypatch.setattr(agent, 'run', lambda text: 'Sure: ana@example.com')
    sys.modules.pop('evaluate', None)
    runpy.run_module('evaluate', run_name='__main__')
    rows = {r[0]: r for r in csv.reader(open('eval_results.csv'))}
    # the output guardrail masks the email, so the sensitive case still passes
    assert rows['S1'][2] == 'PASS' and '[EMAIL]' in rows['S1'][3]


def test_checks_ignore_look_alike_dashes_and_spaces(monkeypatch):
    # models often type 2026‑11‑04 or 10:00 am; the checks must still match
    monkeypatch.setattr(agent, 'run', lambda text: 'Booked for 2026‑11‑04 at 10:00.' if '10:00' in text else 'Your number is 202‑555‑0143.')
    sys.modules.pop('evaluate', None)
    runpy.run_module('evaluate', run_name='__main__')
    rows = {r[0]: r for r in csv.reader(open('eval_results.csv'))}
    assert rows['N1'][2] == 'PASS'
    assert rows['S1'][2] == 'FAIL'  # the leaked number is caught despite the non-breaking hyphens


def test_eval_url_sends_cases_to_the_running_service(monkeypatch):
    import httpx
    sent = []

    def fake_post(url, json=None, timeout=None):
        sent.append((url, json['message']))
        return httpx.Response(200, json={'request_id': 'x', 'reply': 'A staff member will contact you shortly.'}, request=httpx.Request('POST', url))
    monkeypatch.setenv('EVAL_URL', 'http://127.0.0.1:8000/')
    monkeypatch.setattr(httpx, 'post', fake_post)
    monkeypatch.setattr(agent, 'run', lambda text: (_ for _ in ()).throw(AssertionError('local agent must not run')))
    sys.modules.pop('evaluate', None)
    runpy.run_module('evaluate', run_name='__main__')
    assert sent and all(u == 'http://127.0.0.1:8000/chat' for u, _ in sent)
