
import unittest

import functional_tests
import performance_tests

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity = 2)
    
    print("\n*** Functional Tests ***")
    runner.run(functional_tests.suite())
    
    print("\n*** Performance Tests ***")
    runner.run(performance_tests.suite())