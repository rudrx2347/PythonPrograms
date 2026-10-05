import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from importlib import import_module

word_frequency = import_module("Code.20_word_frequency").word_frequency

def test_word_frequency():
    assert word_frequency("hello world hello") == {"hello": 2, "world": 1}

def test_case_insensitive():
    assert word_frequency("Hello hello HELLO") == {"hello": 3}

def test_empty_sentence():
    assert word_frequency("") == {}

def test_multiple_words():
    assert word_frequency("one two two three three three") == {
        "one": 1,
        "two": 2,
        "three": 3,
    }

