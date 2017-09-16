# part of class from p. 291

class Vector2d:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))
    
    def __eq__(self, other):
        return tuple(self) == tuple(other)
