# 6.10 Binary Heap
# needed for Dijkstra's algorithm

# compare to pydspriorityqueue.py

class PriorityQueue:
    def __init__(self):
        # an item is a tuple (distanceToVertex, vertexKey)
        self.heapList = [(0, 0)]  # dummy value
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            # implement min heap
            pass
