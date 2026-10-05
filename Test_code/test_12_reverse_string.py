import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from importlib import import_module

reverse_string = import_module("Code.12_reverse_string").reverse_string

def test_reverse_string():
    assert reverse_string("hello") == "olleh"

def test_empty_string():
    assert reverse_string("") == ""

def test_single_character():
    assert reverse_string("a") == "a"

def test_reverse_sentence():
    assert reverse_string("hello world") == "dlrow olleh"

