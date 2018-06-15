from random import randrange

# p. 968-969

def witness(a, n):
    t = 0 # ???

# https://gist.github.com/Ayrx/5884790

def miller_rabin(n):
    k = 40  # optimal number of rounds according to Stack Overflow
    
    if n <= 1:  # edge cases
        return False
    
    if n == 2:  # the only even prime number
        return True

    if n % 2 == 0:  # even numbers are not prime
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for i in range(k):
        a = randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for j in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def test():
    testeql(miller_rabin(2), True)
    testeql(miller_rabin(1), False)
