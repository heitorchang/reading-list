def filter_out(lst, limit, n):
    # tries all multiples, optimized to begin at the square of the prime
    for i in range(n*n, limit, n):
        try:
            lst.remove(i)
        except:
            pass  # ignore those that are not in the list
    return lst
                   
def sieve(n):
    """Sieve of Erastothenes (slow)"""
    
    s = list(range(n+1)) # assume we want n to be counted
    s = s[2:] # skip 0 and 1
    
    result = [] # store primes

    while s:
        k = s[0]
        result.append(k)
        filter_out(s, s[-1]+1, k)
        s = s[1:]  # advance list
    
    return result  # sieve(n)[-1] will return largest prime that =< n
