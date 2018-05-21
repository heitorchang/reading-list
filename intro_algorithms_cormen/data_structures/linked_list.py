# p. 237

description = """We assume that the lists we are working with are unsorted and doubly linked"""

class LinkedListNode:
    def __init__(self, k):
        self.key = k
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, k):
        x = LinkedListNode(k)
        x.next = self.head
        if self.head:
            self.head.prev = x
        self.head = x
        x.prev = None
        
    def search(self, k):
        x = self.head
        while x and x.key != k:
            x = x.next
        return x
        
    def delete(self, x):
        if x.prev:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next:
            x.next.prev = x.prev

def test():
    L = LinkedList()
    L.insert(1)
    L.insert(2)

    print(L.head.key)
    two = L.search(2)

    L.delete(two)
    print(L.head.next)
