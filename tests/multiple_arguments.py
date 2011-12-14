
import time
from memoize import memoize
import unittest

def multiple_args_normal(some_number,some_string,some_list):
    time.sleep(0.001)
    return some_number
        
@memoize
def multiple_args_memoized(some_number,some_string,some_list):
    time.sleep(0.001)
    return some_number

class MultipleArgumentsTests(unittest.TestCase):

    def test_validate_timing(self):
        start = time.time()
        for _ in range(0,1024):
            multiple_args_normal(3,"hello world",[1,2,3,4,5,7,8,9,10]) 
        stop = time.time()
        normal_duration = (stop-start)*1000
        
        start = time.time()
        for _ in range(0,1024):
            multiple_args_memoized(3,"hello world",[1,2,3,4,5,7,8,9,10]) 
        stop = time.time()
        memoized_duration = (stop-start) * 1000

        self.assertTrue(memoized_duration < normal_duration,
                        msg="normal: %dms < memoized: %dms" % 
                                            (normal_duration,memoized_duration))

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity = 2)
    runner.run(unittest.TestLoader().loadTestsFromTestCase(MultipleArgumentsTests))
    