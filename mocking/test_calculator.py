'''Unit tests for calculator.'''
import os
import sys

from unittest import TestCase
from calculator import Calculator

CURR_DIR = '%s' % os.getcwd()

sys.path.append(CURR_DIR)


class TestCalculator(TestCase):
    '''Test Calculator module.'''
    def setUp(self):
        self.calc = Calculator()

    def test_sum(self):
        '''Test sum operation.'''
        answer = self.calc.add(2, 4)
        self.assertEqual(answer, 6)


# Ref:
# https://semaphoreci.com/community/tutorials/getting-started-with-mocking-in-python

# How to run this file:
# py.test <file_name.py>
