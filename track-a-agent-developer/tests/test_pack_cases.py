import importlib.util, os, glob
import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
FILES = sorted(glob.glob(os.path.join(ROOT, 'industry-packs', '*', 'track-a', 'eval_cases_*.py')))


@pytest.mark.parametrize('path', FILES, ids=[os.path.basename(f) for f in FILES])
def test_pack_eval_sets(path):
    spec = importlib.util.spec_from_file_location('cases', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    cases = mod.CASES
    assert len(cases) == 50
    assert len({c['id'] for c in cases}) == 50
    for c in cases:
        assert set(c) >= {'id', 'type', 'input', 'must', 'must_not'}
        assert c['type'] in {'normal', 'edge', 'adversarial', 'sensitive'}


def test_pack_files_found():
    assert len(FILES) == 2
