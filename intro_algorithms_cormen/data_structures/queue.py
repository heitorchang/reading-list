# p. 235

class Queue:
    """MISSING: bounds checks"""
    
    def __init__(self, size):
        self.array = [None] * size
        self.head = 0
        self.tail = 0

    def enqueue(self, x):
        self.array[self.tail] = x
        if self.tail == len(self.array) - 1:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self):
        x = self.array[self.head]
        if self.head == len(self.array):
            self.head = 0
        else:
            self.head += 1
        return x

def test():
    Q = Queue(5)

    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)
    Q.enqueue(4)
    Q.enqueue(5)
    # Q.enqueue(6)
    # Q.enqueue(7)
    
    testeql(Q.dequeue(), 1)
    
    
