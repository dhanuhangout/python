"""Pytest module to test factorial of a number."""
import os, sys

SRC_DIR = '../programs/'

sys.path.append(SRC_DIR)
import factorial as FactObj

def test_factorial():
    """Tests factorial of a number."""
    assert FactObj.factorial_of_num(4) == 24
