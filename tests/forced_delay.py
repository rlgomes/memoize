
import time
from memoize import memoize

import unittest

class ForcedDelayTests(unittest.TestCase):

    def forced_delay_normal(self,some_number,some_string,some_list):
        time.sleep(0.01)
        return some_number

    # also tests that this works on class objects
    @memoize
    def forced_delay_memoized(self,some_number,some_string,some_list):
        time.sleep(0.01)
        return some_number

    def test_validate_timing(self):
        start = time.time()
        for _ in range(0,10):
            self.forced_delay_normal(3,"hello world",[1,2,3,4,5,7,8,9,10]) 
        stop = time.time()
        normal_duration = (stop-start)*1000
        
        start = time.time()
        for _ in range(0,10):
            self.forced_delay_memoized(3,"hello world",[1,2,3,4,5,7,8,9,10]) 
        stop = time.time()
        memoized_duration = (stop-start)*1000
        
        self.assertTrue(memoized_duration < normal_duration,
                        msg="normal: %dms < memoized: %dms" % 
                                            (normal_duration,memoized_duration))

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity = 2)
    runner.run(unittest.TestLoader().loadTestsFromTestCase(ForcedDelayTests))
