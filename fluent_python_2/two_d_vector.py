'''
Ex. 1-2

v1 = Vector(2, 4)
v2 = Vector(2, 1)
v1 + v2
#> Vector(4, 5)

'''


import math


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        # !r calls repr(). Without it, Vector('0', '1') would print (0, 1)
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
