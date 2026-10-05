from importlib import import_module
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

module = import_module("Code.01_even_odd")
check_func = module.check_even_odd

assert check_func(4) == "Even"
assert check_func(7) == "Odd"
assert check_func(0) == "Even"
assert check_func(-5) == "Odd"

print("All test cases passed.")

