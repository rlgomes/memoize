"""
a set of tests that verify correctness when using memoize

"""

import unittest
import time
import functools

from memoize import memoize

@memoize
def function1(argument1):
    return 0

@memoize
def function2(argument1):
    return 1

class CorrectnessTests(unittest.TestCase):

    def test_two_similar_functions_are_correctly_memoized(self):
        self.assertEqual(function1(1), 0)
        self.assertEqual(function2(1), 1)

        # after initial memoization the results should be the same
        self.assertEqual(function1(1), 0)
        self.assertEqual(function2(1), 1)

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity = 2)
    runner.run(unittest.TestLoader().loadTestsFromTestCase(CorrectnessTests))
