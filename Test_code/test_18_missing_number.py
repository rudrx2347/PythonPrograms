import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from importlib import import_module

find_missing_number = import_module("Code.18_missing_number").find_missing_number

def test_missing_number_middle():
    assert find_missing_number([1, 2, 4, 5], 5) == 3

def test_missing_number_first():
    assert find_missing_number([2, 3, 4, 5], 5) == 1

def test_missing_number_last():
    assert find_missing_number([1, 2, 3, 4], 5) == 5

def test_small_range():
    assert find_missing_number([1], 2) == 2

