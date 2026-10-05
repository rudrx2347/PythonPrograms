import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from importlib import import_module

common_elements = import_module("Code.17_common_elements").common_elements

def test_common_elements():
    assert common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]

def test_no_common_elements():
    assert common_elements([1, 2], [3, 4]) == []

def test_duplicates_are_removed():
    assert common_elements([1, 1, 2, 3], [1, 2, 2]) == [1, 2]

def test_preserves_first_list_order():
    assert common_elements([3, 1, 2], [1, 2, 3]) == [3, 1, 2]

