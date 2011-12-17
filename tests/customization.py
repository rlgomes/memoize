import unittest
import time

from memoize import memoize
from memoize import memoize_with

@memoize
def normal_memoized_function(path, extra):
    return 0

def handle_args(path, extra):
    return path + extra

@memoize_with(handle_args)
def custom_memoized_function(path, extra):
    return 0

class CustomizationTests(unittest.TestCase):

    def test_customization_simple_function(self):
        iterations=1024

        start = time.time()
        for _ in range(0,iterations):
            normal_memoized_function("some path","something else")
        stop = time.time()
        normal_duration = (stop-start)*1000

        start = time.time()
        for _ in range(0,iterations):
            custom_memoized_function("some path","something else")
        stop = time.time()
        custom_duration = (stop-start)*1000

        self.assertTrue(custom_duration < normal_duration, 
                        "custom argument handler must be faster than built-in one")        

    @memoize
    def normal_memoized_function(self, path, extra):
        return 0
    
    def handle_args(self, path, extra):
        return path + extra
    
    @memoize_with(handle_args)
    def custom_memoized_function(self, path, extra):
        return 0
    
    def test_customization_class_method(self):
        iterations=1024

        start = time.time()
        for _ in range(0,iterations):
            self.normal_memoized_function("some path","something else")
        stop = time.time()
        normal_duration = (stop-start)*1000

        start = time.time()
        for _ in range(0,iterations):
            self.custom_memoized_function("some path","something else")
        stop = time.time()
        custom_duration = (stop-start)*1000

        self.assertTrue(custom_duration < normal_duration, 
                        "custom argument handler must be faster than built-in one")        

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity = 2)
    runner.run(unittest.TestLoader().loadTestsFromTestCase(CustomizationTests))
