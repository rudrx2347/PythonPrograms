import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from importlib import import_module

module = import_module("Code.07_primes_in_range")
primes_in_range = module.primes_in_range

def test_primes_in_range():
    assert primes_in_range(1, 10) == [2, 3, 5, 7]

def test_small_range():
    assert primes_in_range(2, 5) == [2, 3, 5]

def test_no_primes():
    assert primes_in_range(8, 10) == []

def test_single_prime_range():
    assert primes_in_range(7, 7) == [7]

