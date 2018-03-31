def addsq(x):
    '''
    Compute the square of an integer by adding abs(value) that many times.
    
    >>> addsq(4)
    16
    >>> addsq(-2)
    4
    >>> addsq(0)
    0
    '''
    n = abs(x)
    sq = 0
    for i in range(n):
        sq += n
    return sq
