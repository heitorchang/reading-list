from math import floor

class Heap:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def left(self):
        return self.left

    def right(self):
        return self.right

# note: heap[0] is unused, set to -1

def parent(i):
    return floor(i/2)

def left(i):
    return 2 * i

def right(i):
    return 2 * i + 1
    
def max_heapify(A, i, len_A):
    lft = left(i)
    rgt = right(i)
    # tamanho_do_heap = len(A) - 1
    tamanho_do_heap = len_A 
    if lft <= tamanho_do_heap and A[lft] > A[i]:
        maior = lft
    else:
        maior = i
    if rgt <= tamanho_do_heap and A[rgt] > A[maior]:
        maior = rgt
    if maior != i:
        A[i], A[maior] = A[maior], A[i]
        max_heapify(A, maior, len_A)

def build_max_heap(A):
    heap = [-1] + A[:]  # make a copy
    for i in range(floor(len(A) / 2), 0, -1):
        max_heapify(heap, i, len(heap) - 1) 
    return heap 
    
def heapsort(A):
    h = build_max_heap(A)
    len_h = len(h) - 1
    for j in loop.downto(len_h, 2):
        # print(h) 
        h[1], h[j] = h[j], h[1]
        len_h -= 1
        max_heapify(h, 1, len_h)
    return h 

# p. 117

a = [16,14,10,8,7,9,3,2,4,1]
