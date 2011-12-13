
import time
from memoize import memoize
import unittest

def lookup_path_normal(path):
    if path == "": path = "/"
    something = [ ]
    
    for path in path.split("/"):
        something.append(path)
        
    return ''.join(something)

@memoize
def lookup_path_memoized(path):
    if path == "": path = "/"
    something = [ ]
    
    for path in path.split("/"):
        something.append(path)
        
    return ''.join(something)


class LookupTests(unittest.TestCase):

    def forced_delay_normal(self,some_number,some_string,some_list):
        time.sleep(0.1)
        return some_number

    @memoize
    def forced_delay_memoized(self,some_number,some_string,some_list):
        time.sleep(0.1)
        return some_number

    def test_validate_timing(self):
        test_path = "some/long/ass/path/to/test/this/shit/out"
        
        start = time.time()
        for _ in range(0,200*1024):
            lookup_path_normal(test_path)
        stop = time.time()
        normal_duration = (stop-start) * 1000
        print("\nlookup_path_normal: %dms" % ((stop-start)*1000))
        
        start = time.time()
        for _ in range(0,200*1024):
            lookup_path_memoized(test_path)
        stop = time.time()
        memoized_duration = (stop-start) * 1000
        print("\nlookup_path_memoize: %dms" % ((stop-start)*1000))

        
        self.assertTrue(memoized_duration < normal_duration)

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity = 2)
    runner.run(unittest.TestLoader().loadTestsFromTestCase(LookupTests))
