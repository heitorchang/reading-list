def gcd(m, n):
    
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n
    

class Fraction:
    
    def __init__(self, top, bottom):

        self.num = top
        self.den = bottom


    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den

        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

        
    def __str__(self):
        
        return str(self.num) + "/" + str(self.den)


    def __repr__(self):
        
        return "Fraction({}, {})".format(str(self.num), str(self.den))


    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum
