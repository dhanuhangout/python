import os, sys

src_dir = '../programs/'

sys.path.append(src_dir)
import factorial as FactObj

def test_factorial():
    assert FactObj.factorial_of_num(4) == 24
