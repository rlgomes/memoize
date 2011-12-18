
import unittest

from forced_delay import ForcedDelayTests 
from recursive import RecursiveTests 
from multiple_arguments import MultipleArgumentsTests
from customization import CustomizationTests
from comparison import ComparisonTests

def suite():
    suite = unittest.TestSuite()
    
    suite.addTest(unittest.makeSuite(ForcedDelayTests))
    suite.addTest(unittest.makeSuite(RecursiveTests))
    suite.addTest(unittest.makeSuite(MultipleArgumentsTests))

    suite.addTest(unittest.makeSuite(CustomizationTests))
    suite.addTest(unittest.makeSuite(ComparisonTests))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity = 2)
    runner.run(suite())