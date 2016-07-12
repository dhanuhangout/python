"""Pytest module to test programs present programs folder."""
import os, sys

C_DIR = os.getcwd()
SRC_DIR = '%s/programs/' % C_DIR

sys.path.append(SRC_DIR)
import factorial as FactObj
import fibonacci as FiboObj

def test_factorial():
    """Tests factorial of a number."""
    assert FactObj.factorial_of_num(4) == 24

def test_fibonacci():
    """pytest to verify fibonacci series."""
    assert FiboObj.fibonacci_series(5) == [0, 1, 1, 2, 3, 5]
