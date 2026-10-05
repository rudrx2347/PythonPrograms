import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from importlib import import_module

character_frequency = import_module("Code.14_char_frequency").character_frequency

def test_character_frequency():
    assert character_frequency("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}

def test_repeated_character():
    assert character_frequency("aaa") == {"a": 3}

def test_empty_string():
    assert character_frequency("") == {}

def test_spaces_are_counted():
    assert character_frequency("a a") == {"a": 2, " ": 1}

