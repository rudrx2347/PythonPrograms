import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from importlib import import_module

count_vowels_consonants = import_module("Code.11_vowels_consonants").count_vowels_consonants

def test_basic_text():
    assert count_vowels_consonants("Hello") == (2, 3)

def test_all_vowels():
    assert count_vowels_consonants("aeiou") == (5, 0)

def test_all_consonants():
    assert count_vowels_consonants("bcdf") == (0, 4)

def test_ignores_spaces_and_digits():
    assert count_vowels_consonants("Hello 123!") == (2, 3)

