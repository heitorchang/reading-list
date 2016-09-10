# p. 51 ex. 2.4.4, 2.4.5

# commutative: a + b = b + a

# associative: (a + b) + c = a + (b + c)

# commutative but not associative
# rock-paper-scissors
def rps(a, b):
    if a == 'r' and b == 'p':
        return 'p'
    elif a == 'r' and b == 's':
        return 'r'
    elif a == 'p' and b == 'r':
        return 'p'
    elif a == 'p' and b == 's':
        return 's'
    elif a == 's' and b == 'r':
        return 'r'
    elif a == 's' and b == 'p':
        return 's'
    else:
        return a

def test_rps():
    print("The VS (versus) operator uses RPS rules.")
    print("It is commutative but not associative (order matters)")
    print("Clearly r VS p is the same as p VS r")
    print("(r VS p) VS s : %s" % (rps(rps('r', 'p'), 's')))
    print("r VS (p VS s) : %s" % (rps('r', rps('p', 's'))))
    
# associative, but not commutative : 
def x_only(x, y):
    return x

def test_x_only():
    print("The contrived function discards the right-hand side argument")
    print("It is not commutative, because flipping arguments results in")
    print("the right-hand side argument being discarded.")
    print("(3 XO 5) XO 7 = %s" % (x_only(x_only(3, 5), 7)))
    print("3 XO (5 XO 7) = %s" % (x_only(3, x_only(5, 7))))
    
