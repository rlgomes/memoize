"""
This is just a comparison tests between the very basic and limited memoized 
decorator that is in the python documentation and the memoize decorator that is
part of the library being distributed in this package.
"""
import unittest
import time
import functools

from memoize import memoize_with 

"""
The following class taken from python's online documentation on decorators and 
how to use them.
"""
class memoized(object):
    """Decorator that caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned, and
    not re-evaluated.
    """
    def __init__(self, func):
        self.func = func
        self.cache = {}
   
    def __call__(self, *args):
        try:
            return self.cache[args]
        except KeyError:
            value = self.func(*args)
            self.cache[args] = value
            return value
        except TypeError:
            # uncachable -- for instance, passing a list as an argument.
            # Better to not cache than to blow up entirely.
            return self.func(*args)
        
    def __repr__(self):
        """Return the function's docstring."""
        return self.func.__doc__
    
    def __get__(self, obj, objtype):
        """Support instance methods."""
        return functools.partial(self.__call__, obj)

def normal_function(path, extra):
    return 0

def handle_normal_memoize_function(path,extra):
    return path + extra

@memoize_with(handle_normal_memoize_function)
def normal_memoize_function(path, extra):
    return 0

@memoized
def normal_memoized_function(path, extra):
    return 0

class ComparisonTests(unittest.TestCase):

    def test_customization_simple_function(self):
        iterations=500*1024

        start = time.time()
        for _ in range(0,iterations):
            normal_memoized_function("some path","something else")
        stop = time.time()
        memoized_duration = (stop-start)*1000
        
        start = time.time()
        for _ in range(0,iterations):
            normal_memoize_function("some path","something else")
        stop = time.time()
        memoize_duration = (stop-start)*1000
       
        print("\n@memoize: %dms" % memoize_duration)
        print("\n@memoized: %dms" % memoized_duration)
        print("\n@memoized faster than @memoize by %fx" % 
              (memoize_duration/memoized_duration))

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity = 2)
    runner.run(unittest.TestLoader().loadTestsFromTestCase(ComparisonTests))
