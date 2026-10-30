import pytest

rag = pytest.importorskip('rag')


def test_short_text_is_one_chunk():
    assert rag.chunk('hello', size=500, overlap=100) == ['hello']


def test_exact_size_has_no_tiny_duplicate():
    text = 'x' * 500
    assert rag.chunk(text, size=500, overlap=100) == [text]


def test_overlap_and_coverage():
    text = ''.join(chr(97 + i % 26) for i in range(1200))
    parts = rag.chunk(text, size=500, overlap=100)
    assert [len(p) for p in parts] == [500, 500, 400]
    assert parts[0][-100:] == parts[1][:100]
    assert parts[-1].endswith(text[-50:])


def test_empty_text():
    assert rag.chunk('', size=500, overlap=100) == []
