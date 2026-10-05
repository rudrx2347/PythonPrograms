import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from importlib import import_module
import pytest

second_largest = import_module("Code.15_second_largest").second_largest

def test_second_largest():
    assert second_largest([10, 5, 8, 20]) == 10

def test_second_largest_unsorted():
    assert second_largest([3, 9, 1, 7]) == 7

def test_duplicates():
    assert second_largest([10, 10, 8, 5]) == 8

def test_negative_numbers():
    assert second_largest([-1, -5, -3]) == -3

def test_not_enough_unique_numbers():
    with pytest.raises(ValueError):
        second_largest([5, 5, 5])

