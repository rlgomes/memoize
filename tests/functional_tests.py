
import unittest

from forced_delay import ForcedDelayTests 
from recursive import RecursiveTests 
from lookup import LookupTests
from multiple_arguments import MultipleArgumentsTests

def suite():
    suite = unittest.TestSuite()
    
    suite.addTest(unittest.makeSuite(ForcedDelayTests))
    suite.addTest(unittest.makeSuite(RecursiveTests))
    suite.addTest(unittest.makeSuite(LookupTests))
    suite.addTest(unittest.makeSuite(MultipleArgumentsTests))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity = 2)
    runner.run(suite())