from itertools import repeat

def my_square(n):
    """
    my_square tries to sum a number repeated as many times as itself
    
    >>> my_square(3)
    9
    >>> my_square(-1)
    1
    >>> my_square(7)
    49
    """
    
    m = abs(n)
    return sum(repeat(m, m))

def my_sub_one(n):
    """
    >>> my_sub_one(9)
    8
    """
    return n - 1

def my_range_plus_one(n):
    """
    >>> my_range_plus_one(10) # doctest: +ELLIPSIS
    [0, 1, 2, ..., 10]
    """
    return list(range(n+1))
