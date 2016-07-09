import os, sys

SRC_DIR = '../programs/'

sys.path.append(SRC_DIR)
import fibonacci as FiboObj

def test_fibonacci():
    assert FiboObj.fibonacci_series(5) == [0,1,1,2,3,5]
