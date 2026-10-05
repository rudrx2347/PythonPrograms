import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from importlib import import_module

is_palindrome_string = import_module("Code.13_palindrome_string").is_palindrome_string

def test_palindrome_string():
    assert is_palindrome_string("madam") is True

def test_not_palindrome_string():
    assert is_palindrome_string("hello") is False

def test_case_insensitive():
    assert is_palindrome_string("Madam") is True

def test_empty_string():
    assert is_palindrome_string("") is True

