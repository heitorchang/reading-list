# p. 519

def add_coro(a):
    print('started, a =', a)
    b = yield a
    print('received b =', b)
    c = yield a + 29
    print('received c =', c)
    
