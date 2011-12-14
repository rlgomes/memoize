
from memoize import memoize
import time
import unittest

def func_normal(number,string,elements):
    return 0

@memoize
def func_memoized(number,string,elements):
    return 0

class OverheadTests(unittest.TestCase):

    def test_validate_memoize_overhead(self):
        
        iterations=200*1024
        start = time.time()
        for _ in range(iterations):
            func_normal(0,"blah",[1,2,3])
        stop = time.time()
        normal_duration = (stop-start) * 1000
        
        start = time.time()
        for _ in range(iterations):
            func_memoized(0,"blah",[1,2,3])
        stop = time.time()
        memoized_duration = (stop-start) * 1000
       
        overhead = (memoized_duration-normal_duration)*1000/iterations
       
        # worst case scenario I'd like the overhead of the memoize library to 
        # take no longer than 10 nanoseconds (this should be measured in CPU
        # ticks) 
        self.assertTrue(overhead < 10,
                        msg="overhead > 10ns, actual: %fns" % overhead)

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity = 2)
    runner.run(unittest.TestLoader().loadTestsFromTestCase(OverheadTests))


