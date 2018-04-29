class Heap:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def max_heapify(self):
        L = getattr(self, 'left', None)
        R = getattr(self, 'right', None)

        left_val = getattr(L, 'value', float('-inf'))
        right_val = getattr(R, 'value', float('-inf'))
                                    
        if left_val > right_val and left_val > self.value:
            self.value, self.left.value = self.left.value, self.value
            self.left.max_heapify()
        elif right_val > left_val and right_val > self.value:
            self.value, self.right.value = self.right.value, self.value
            self.right.max_heapify()
            
        # if L and self.left.value > self.value
        #     self.value, self.left.value = self.left.value, self.value
        #     self.left.max_heapify()
        # elif R and self.right.value > self.value and self.right.value > self.left.value:
        #    self.value, self.right.value = self.right.value, self.value
        #    self.right.max_heapify()
        
        # if L and self.left.value > self.value:
        #    largest = "L"
        #    largest_value = self.left.value
        #else:
        #    largest = "self"
        #    largest_value = self.value

        #if R and self.right.value > largest_value:
        #    largest = "R"

        #if largest == "L":
        #    self.value, self.left.value = self.left.value, self.value
        #    self.left.max_heapify()
        #elif largest == "R":
        #    self.value, self.right.value = self.right.value, self.value
        #    self.right.max_heapify()

    def build_max_heap(self):
        q = []
        visited = [self]
        q.insert(0, self)
        while q:
            node = q.pop()
            L = getattr(node, 'left', None)
            R = getattr(node, 'right', None)
            if L:
                q.insert(0, node.left)
                visited.insert(0, node.left)
            if R:
                q.insert(0, node.right)
                visited.insert(0, node.right)
        #return visited
        for node in visited:            
            node.max_heapify()

    def all_but_top(self):
        q = []
        visited = []
        q.insert(0, self)
        while q:
            node = q.pop()
            if node.left:
                q.insert(0, node.left)
                visited.append(node.left.value)
            if node.right:
                q.insert(0, node.right)
                visited.append(node.right.value)
        return visited                
            
    def show_tree(self):
        q = []
        q.insert(0, self)
        repr = ""
        levels = [1,2,4,8,16,32]
        trigger = [1,3,7,15,31,63]
        ct = 0
        while q:
            if ct in trigger:
                repr += "\n"
            node = q.pop()
            repr += str(node.value) + " "
            L = getattr(node, 'left', None)
            R = getattr(node, 'right', None)
            if L:
                q.insert(0, node.left)
            if R:
                q.insert(0, node.right)
            ct += 1
        print(repr)
        # return str(self.value)

    def __repr__(self):
        return str(self.value)
        
def make_heap_node(A, i):
    root = Heap(A[i])
    if 2*i < len(A):
        root.left = Heap(A[2*i])
    if (2*i) + 1 < len(A):
        root.right = Heap(A[(2*i) + 1])
    return root
    
def array_to_heap(arr_zero_indexed):
    arr_len_zero = len(arr_zero_indexed)
    arr = [0] + arr_zero_indexed
    arr_len = len(arr)
    
    heaps = []
    for i in range(arr_len):
        # make each element a unique heap
        heaps.append(Heap(arr[i]))

    for i in range(arr_len // 2, 0, -1):
        # connect heaps
        if 2 * i < arr_len:
            # print("connect heap left ", i, "to", 2 * i)
            heaps[i].left = heaps[2 * i]
        if 2 * i + 1 < arr_len:
            # print("connect heap right ", i, "to", 2 * i + 1)
            heaps[i].right = heaps[2 * i + 1]
    return heaps[1]

def test_heap():
    h = Heap(16)
    h.left = Heap(4)
    h.right = Heap(10)
    
    h.left.left = Heap(14)
    h.left.right = Heap(7)
    
    h.right.left = Heap(9)
    h.right.right = Heap(3)
    
    h.left.left.left = Heap(2)
    h.left.left.right = Heap(8)
    h.left.right.left = Heap(1)
    return h
    
def test_heap_2():
    h = Heap(4)
    h.left = Heap(1)
    h.right = Heap(3)

    h.left.left = Heap(2)
    h.left.right = Heap(16)

    h.right.left = Heap(9)
    h.right.right = Heap(10)

    h.left.left.left = Heap(14)
    h.left.left.right = Heap(8)

    h.left.right.left = Heap(7)
    return h

def my_heapsort(A):
    result = []
    h = array_to_heap(A)

    for i in range(len(A)):
    
        h.build_max_heap()
        # print("top of heap", h.value)
        result.insert(0, h.value)
    
        rest = h.all_but_top()
        # print("rest", rest)

        if rest:
            h = array_to_heap(rest)
    return result
