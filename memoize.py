
global memoize_cache
memoize_cache = {}

class memoize(object):
    '''
    Memoize the function being decorated so that subsequent calls with the same
    arguments are pulled from a cache that contains the previously collected 
    result. When using this decorator you can easily add memoization capabilities
    to your function without cluttering it with code that is prone to errors.
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
    
class memoize_with(memoize):

    def __init__(self, handle_args):
        """
        Memoize the function being decorated but specify the function to handle 
        the arguments and keywords being passed to your function. This handle_args
        function is responsible for taking the arguments that your function 
        accepts and returning a simple string that uniquely identifies those
        arguments. Here's a small example:
        
        def handle_args(path, extra):
            return path + extra

        @memoize_with(handle_args)
        def custom_memoized_function(path, extra):
            return 0
            
        There's not much more to it and just by using this simple argument 
        handler you can speed up the execution vs the normal built-in argument 
        handler by 30%
        """
        self.handle_args = handle_args
   
    def __call__(self, function):
        parent = self
        
        def new_f(*args, **kwargs): 
            global memoize_cache
            if kwargs == {}:
                argkey = parent.handle_args(*args)
            else:
                argkey = parent.handle_args(*args,**kwargs)
                
            if argkey in memoize_cache.keys():
                return memoize_cache[argkey]
            else:
                ret = function(*args, **kwargs)
                memoize_cache[argkey] = ret
                return ret
            
        return new_f
        