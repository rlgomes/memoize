
import unittest

from overhead import OverheadTests

def suite():
    suite = unittest.TestSuite()
    
    suite.addTest(unittest.makeSuite(OverheadTests))
    
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity = 2)
    runner.run(suite())