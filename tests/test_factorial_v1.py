import os, sys

SRC_DIR = '../programs/'

sys.path.append(SRC_DIR)
import factorial as FactObj

def test_factorial():
    assert FactObj.factorial_of_num(4) == 24
