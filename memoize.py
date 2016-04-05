"""
The basic memoize decorator can be used quickly by just placing the "@memoize"
decorator on the line above the function definition and there is also a 
"memoize_with" which allows the user to define the argument to unique string id
transformation to be used when identify that the arguments being passed to your
function are indeed the same argument combination that was used a while ago.
"""

import functools

global MEMOIZE_CACHE
MEMOIZE_CACHE = {}

class memoize(object):
    '''
    Memoize the function being decorated so that subsequent calls with the same
    arguments are pulled from a cache that contains the previously collected 
    result. When using this decorator you can easily add memoization capabilities
    to your function without cluttering it with code that is prone to errors.
    '''
    def __init__(self, function):
        self.__f = function
        self.__f_get = self.__f.__get__
        functools.update_wrapper(self, function)
   
    def __call__(self, *args, **kwargs):
        func_name = getattr(self.__f, '__name__', None) or self.__f.func_name
        argkey = (func_name, str(args), str(kwargs))
            
        if argkey in MEMOIZE_CACHE.keys():
            return MEMOIZE_CACHE[argkey]
        else:
            ret = self.__f(*args, **kwargs)
            MEMOIZE_CACHE[argkey] = ret
            return ret
        
    def __get__(self, obj, type=None):
        if obj is None:
            return self
        
        new_func = self.__f_get(obj, type)
        return self.__class__(new_func) 
    
class memoize_with(memoize):

    def __init__(self, hash_args):
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
        self.hash_args = hash_args
   
    def __call__(self, function):
        parent = self
        
        def new_f(*args, **kwargs): 
            """ 
            memoiziation magic
            """
            if kwargs == {}:
                argkey = parent.hash_args(*args)
            else:
                argkey = parent.hash_args(*args, **kwargs)
                
            if argkey in MEMOIZE_CACHE.keys():
                return MEMOIZE_CACHE[argkey]
            else:
                ret = function(*args, **kwargs)
                MEMOIZE_CACHE[argkey] = ret
                return ret
            
        return new_f
        
