from setuptools import setup

setup (
    name='memoize2',
    version='0.1.1',
    author='Rodney Gomes',
    author_email='rodneygomes@gmail.com',
    url='https://github.com/rlgomes/memoize',
    test_suite="tests",
    keywords = ['memoize', 'library'],
    py_modules = ['memoize'],
    license='Apache 2.0 License',
    description='The memoize library can be used to quickly add the memoization feature to any existing function so that you can cache previously calculated results for the same arguments but don\'t have to "clutter" your function code to add the memoization feature into your function.'
)
