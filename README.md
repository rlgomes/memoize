Introduction
------------

[![Build Status](https://travis-ci.org/rlgomes/memoize.png)](https://travis-ci.org/rlgomes/memoize)

Using memoize
-------------

From wikipedia:

> In computing, memoization is an optimization technique used primarily to speed 
> up computer programs by having function calls avoid repeating the calculation of
> results for previously processed inputs.

The memoize library can be used to quickly add the memoization feature to any 
existing function so that you can cache previously calculated results for the 
same arguments but don't have to "clutter" your function code to add the 
memoization feature into your function.

There is a pretty simple implementation of such a decorator in some of python's 
documentation but the implementation itself is quite basic and won't handle a 
few of the use cases resolved with this simple decorator. Here is a list of the 
reasons why I wouldn't use the example "memoized" decorator from the python 
documentation:

 1. It relies on exceptions being raised for it to decide to cache the current 
    results from the function you had decorated. Relying on exceptions to be 
    thrown to tests if something is on a cache is a bad design IMHO.
      
 2. The memoized decorator doesn't handle list types and a few others while
    the memoize decorator can be used on any type that can be converted into 
    a string by the str() function.
    
 3. The memoized decorator also doesn't handle the keyword arguments 
 
 4. The memoize decorator allows you to customize your argument hashing function
    which controls how you match the arguments during the caching of results
    previously calculated. The memoized decorator doesn't have this feature.

The basic memoize decorator can be used quickly by just placing the "@memoize"
decorator on the line above the function definition and there is also a 
"memoize_with" which allows the user to define the argument to unique string id
transformation to be used when identify that the arguments being passed to your
function are indeed the same argument combination that was used a while ago.

Lets first show a simple example of a very recursive function you may find a 
little familiar:

```python
def recursive_function_normal(arg):
    if arg <= 0: return 1
    if arg == 1: return 1
    return recursive_function_normal(arg-1) + recursive_function_normal(arg-2)
```

Now this function seems innocent enough but if you have a close look at the 
recursive calls within this function you'll realize its quite a complex sum
of the previous elements with the value of the current element. Now before 
adding the memoize decorator lets see how well this function scales:

```
recursive_function_normal(10) took 0ms
recursive_function_normal(20) took 13ms
recursive_function_normal(30) took 688ms
recursive_function_normal(32) took 1605ms
```

That does not look promising at all if we wanted to calculate something like the
value for 100 or 200 it would probably take a few hours. Now with memoization 
applied to this same function, like so:

```python
@memoize
def recursive_function_memoized(arg):
    if arg <= 0: return 1
    if arg == 1: return 1
    return recursive_function_memoized(arg-1) + recursive_function_memoized(arg-2)
```

Here are the numbers:

```
recursive_function_memoized(10) took 0ms
recursive_function_memoized(20) took 0ms
recursive_function_memoized(30) took 0ms
recursive_function_memoized(32) took 0ms
```

Even from scratch calculation 100 is very fast:

```
recursive_function_memoized(100) took 2ms
```

You might be scratching your head thinking this is impossible but just remember 
that after you've calculated the value for 10, 20 and 30 when you issue the 
call for 100 you only have a few "new" values to calculate while all the others
are pulled straight off the memoization cache.

Of course there are situations where the normal memoize decorator isn't efficient
enough when handling multiple arguments to your functions and when you have a 
good grasp on how to uniquely encode the arguments being passed to your function
in a simple string (ie hash) you can replace the built-in "hashing" mechanism 
with your own custom one by using the "@memoize_with(hash_args)" declaration
and then defining the hash_args with the same signature as the function you're
attempting to memoize. Here is a small example of how to write your own argument
hashing function.

Installing
----------

```
python setup.py install
```

or install directly from github with:

```
pip install -e git+git://github.com/rlgomes/memoize.git#egg=memoize
```

Running Built-In Tests
-----------------------

After installing the memoize library you can go to the tests directory and run 
all the tests by executing:

```
cd tests
python all_tests.py
```

License
-------

Apache 2.0 License (http://www.apache.org/licenses/LICENSE-2.0.html)
