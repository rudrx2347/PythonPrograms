import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from importlib import import_module

reverse_number = import_module("Code.08_reverse_number").reverse_number

def test_reverse_positive():
    assert reverse_number(12345) == 54321

def test_reverse_zero():
    assert reverse_number(0) == 0

def test_reverse_negative():
    assert reverse_number(-123) == -321

def test_reverse_trailing_zero():
    assert reverse_number(1200) == 21

