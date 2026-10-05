import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from importlib import import_module

find_duplicates = import_module("Code.19_find_duplicates").find_duplicates

def test_find_duplicates():
    assert find_duplicates([1, 2, 2, 3, 3, 3]) == [2, 3]

def test_no_duplicates():
    assert find_duplicates([1, 2, 3]) == []

def test_duplicate_once():
    assert find_duplicates([5, 5]) == [5]

def test_preserves_duplicate_order():
    assert find_duplicates([3, 1, 3, 2, 1, 2]) == [3, 1, 2]

