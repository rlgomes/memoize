
import unittest

def suite():
    suite = unittest.TestSuite()
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity = 2)
    runner.run(suite())