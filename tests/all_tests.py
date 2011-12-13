
import unittest

import functional_tests

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity = 2)
    print("*** Functional Tests ***")
    runner.run(functional_tests.suite())