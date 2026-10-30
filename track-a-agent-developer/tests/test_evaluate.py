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
