class MQueue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    # in reality, enqueue should be O(1) but since we use the
    # built-in list, it is O(n)
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __repr__(self):
        return self.items
