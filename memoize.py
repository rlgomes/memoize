
global memoize_cache
memoize_cache = {}

class memoize(object):
    '''
    '''

    def __init__(self, function):
        self.__f = function
   
    def __call__(self, *args, **kwargs): 
        global memoize_cache
        argkey = (str(args),str(kwargs))
            
        if argkey in memoize_cache.keys():
            return memoize_cache[argkey]
        else:
            ret = self.__f(*args, **kwargs)
            memoize_cache[argkey] = ret
            return ret
        
    def __get__(self, obj, type=None):
        if obj is None:
            return self
        
        new_func = self.__f.__get__(obj, type)
        return self.__class__(new_func) 