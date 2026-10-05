import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from importlib import import_module

sum_of_digits = import_module("Code.10_sum_of_digits").sum_of_digits

def test_sum_digits():
    assert sum_of_digits(1234) == 10

def test_zero():
    assert sum_of_digits(0) == 0

def test_negative_number():
    assert sum_of_digits(-123) == 6

def test_single_digit():
    assert sum_of_digits(7) == 7

