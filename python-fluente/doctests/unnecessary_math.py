# http://pythontesting.net/framework/doctest/doctest-introduction/

'''
module showing how doctests can be included with source code
'''

def multiply(a, b):
    """
    >>> multiply(4, 3)
    12
    >>> multiply('a', 3)
    'aaa'
    """
    return a * b
