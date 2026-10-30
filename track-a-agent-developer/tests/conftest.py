"""Shared test setup: fake keys, no network, project folder on the import path."""
import os, sys, types, json
import pytest

os.environ.setdefault('LLM_API_KEY', 'test-key-not-real')
os.environ.setdefault('LLM_BASE_URL', 'http://127.0.0.1:9/v1')
os.environ.setdefault('MODEL', 'fake-model')

HERE = os.path.dirname(__file__)
PROJECT = os.path.abspath(os.path.join(HERE, '..', 'project'))
sys.path.insert(0, PROJECT)


@pytest.fixture(autouse=True)
def _tmp_cwd(tmp_path, monkeypatch):
    """Run each test in a temp folder so usage.csv and logs do not pile up."""
    monkeypatch.chdir(tmp_path)


def make_msg(content=None, tool_calls=None):
    """Build an object shaped like an OpenAI chat message."""
    calls = None
    if tool_calls:
        calls = [types.SimpleNamespace(
            id=f'call_{i}',
            function=types.SimpleNamespace(name=name, arguments=args))
            for i, (name, args) in enumerate(tool_calls)]

    class Msg(types.SimpleNamespace):
        def model_dump(self, exclude_none=False):
            d = {'role': 'assistant', 'content': self.content}
            if self.tool_calls:
                d['tool_calls'] = [{'id': c.id, 'type': 'function',
                                    'function': {'name': c.function.name,
                                                 'arguments': c.function.arguments}}
                                   for c in self.tool_calls]
            return {k: v for k, v in d.items() if not (exclude_none and v is None)}

    return Msg(content=content, tool_calls=calls)


def make_resp(msg, prompt_tokens=10, completion_tokens=5):
    return types.SimpleNamespace(
        choices=[types.SimpleNamespace(message=msg)],
        usage=types.SimpleNamespace(prompt_tokens=prompt_tokens,
                                    completion_tokens=completion_tokens))


class FakeCompletions:
    """Returns scripted replies in order and records every request."""
    def __init__(self, replies):
        self.replies = list(replies)
        self.calls = []

    def create(self, **kwargs):
        self.calls.append(kwargs)
        return self.replies.pop(0)


def fake_client(replies):
    comp = FakeCompletions(replies)
    return types.SimpleNamespace(chat=types.SimpleNamespace(completions=comp)), comp
