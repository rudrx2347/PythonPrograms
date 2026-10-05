import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from importlib import import_module

check_even_odd = import_module("Code.01_even_odd").check_even_odd

def test_even_number():
    assert check_even_odd(10) == "Even"

def test_odd_number():
    assert check_even_odd(7) == "Odd"

def test_zero():
    assert check_even_odd(0) == "Even"

def test_negative_even():
    assert check_even_odd(-4) == "Even"

def test_negative_odd():
    assert check_even_odd(-5) == "Odd"

