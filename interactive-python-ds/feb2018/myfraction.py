def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
        
class MyFraction:
    def __init__(self, top, bottom):
        g = gcd(top, bottom)
        self.num = top // g
        self.denom = bottom // g
        

    def __add__(self, other):
        newNum = self.num * other.denom + self.denom * other.num
        newDenom = self.denom * other.denom

        return MyFraction(newNum, newDenom)

    # Shallow equality between two references means they refer to the
    # same object

    # Deep equality is equality by the same value(s)

    def __eq__(self, other):
        return self.num * other.denom == self.denom * other.num
        
    def __str__(self):
        return "%d/%d" % (self.num, self.denom)

    def __repr__(self):
        return self.__str__()

def test():
    pass
