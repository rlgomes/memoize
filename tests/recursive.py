
from memoize import memoize
import time
import unittest

def recursive_function_normal(arg):
    if arg <= 0: return 1
    if arg == 1: return 1
    return recursive_function_normal(arg-1) + recursive_function_normal(arg-2)

@memoize
def recursive_function_memoized(arg):
    if arg <= 0: return 1
    if arg == 1: return 1
    return recursive_function_memoized(arg-1) + recursive_function_memoized(arg-2)

class RecursiveTests(unittest.TestCase):

    def test_validate_timing(self):
        start = time.time()
        for value in [10,20,30]:
            recursive_function_normal(value)
        stop = time.time()
        normal_duration = (stop-start) * 1000
        
        start = time.time()
        for value in [10,20,30]:
            recursive_function_memoized(value)
        stop = time.time()
        memoized_duration = (stop-start) * 1000
        
        self.assertTrue(memoized_duration < normal_duration,
                        msg="normal: %dms < memoized: %dms" % 
                                            (normal_duration,memoized_duration))

    def test_validate_return(self):
        for value in [1,2,3,4,5,20,30]:
            self.assertEquals(recursive_function_normal(value),
                              recursive_function_memoized(value))

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity = 2)
    runner.run(unittest.TestLoader().loadTestsFromTestCase(RecursiveTests))


