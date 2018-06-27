# p. 517
def simple_coroutine():
    print("-> coro started")
    x = yield
    print('-> coro received', x)
    
