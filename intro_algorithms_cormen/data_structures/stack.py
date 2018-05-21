# p. 233

class Stack:
    def __init__(self ,size):
        self.array = [None] * size
        self.top = 0

    def push(self, x):
        self.top += 1
        self.array[self.top] = x

    def pop(self):
        if self.empty():
            raise IndexError("stack underflow")
        else:
            self.top -= 1
            return self.array[self.top+1]

    def empty(self):
        if self.top == 0:
            return True
        return False


def test():
    S = Stack(16)
    
    testeql(S.empty(), True)

    S.push(3)
    S.push(9)

    testeql(S.pop(), 9)
    testeql(S.pop(), 3)
    
