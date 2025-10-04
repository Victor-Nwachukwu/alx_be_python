import subprocess
import sys
import pytest
from robust_division_calculator import safe_divide

# ---------- UNIT TESTS ----------

def test_safe_divide_success():
    result = safe_divide(12, 2)
    assert result == 6.0

def test_safe_divide_zero_division():
    result = safe_divide(10, 0)
    assert result == "Error: Cannot divide by zero."

def test_safe_divide_non_numeric():
    result = safe_divide("abc", 5)
    assert result == "Error: Please enter numeric values only."

def test_safe_divide_float_input():
    result = safe_divide("7.5", "2.5")
    assert result == 3.0


# ---------- INTEGRATION TESTS (main.py) ----------

def run_main(args):
    """Helper to run main.py and capture output"""
    result = subprocess.run(
        [sys.executable, "main.py"] + args,
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def test_main_success():
    output = run_main(["12", "2"])
    assert output == "The result of the division is 6.0"

def test_main_zero_division():
    output = run_main(["5", "0"])
    assert output == "Error: Cannot divide by zero."

def test_main_non_numeric():
    output = run_main(["abc", "3"])
    assert output == "Error: Please enter numeric values only."

def test_main_usage_message():
    """When no args are provided, main.py should print usage message"""
    result = subprocess.run(
        [sys.executable, "main.py"],
        capture_output=True,
        text=True
    )
    assert "Usage: python main.py <numerator> <denominator>" in result.stdout.strip()
