import os, sys

from unittest import TestCase

CURR_DIR = '%s' % os.getcwd()

sys.path.append(CURR_DIR)
# from calculator import Calculator
from mock import patch


class TestCalculator(TestCase):

    @patch('.Calculator.sum', return_value=9)
    def test_sum(self, sum):
        self.assertEqual(sum(2,3), 9)


# Ref:
# https://semaphoreci.com/community/tutorials/getting-started-with-mocking-in-python

# How to run this file:
# py.test <file_name.py>
