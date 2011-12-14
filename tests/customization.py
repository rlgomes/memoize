
import time
from memoize import memoize
import unittest

@memoize
def some_function(path):
    return 0

class CustomizationTests(unittest.TestCase):

    def test_validate_timing(self):
        some_function("blah")
        pass

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity = 2)
    runner.run(unittest.TestLoader().loadTestsFromTestCase(CustomizationTests))
