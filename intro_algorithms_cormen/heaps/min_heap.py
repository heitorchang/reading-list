# p. 154

from heap import left, right, parent
from random import shuffle

def min_heapify(A, i):
    """Given array A and index i, min_heapify assumes left(i) and right(i) are min-heaps, but A[i] might be larger than its children."""

    L = left(i)
    R = right(i)

    if L <= len(A) - 1 and A[L] < A[i]:  # assume len(A) is A.heap_size
        smallest = L
    else:
        smallest = i

    if R <= len(A) - 1 and A[R] < A[smallest]:
        smallest = R
        
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        min_heapify(A, smallest)

def build_min_heap(A):
    for i in range((len(A) // 2) - 1, -1, -1):
        min_heapify(A, i)


def heapsort(A):
    """p. 160, using a new array for the result. See max_heap.py"""
    result = []
    build_min_heap(A)
    print(A)
    for i in range(len(A) - 1, -1, -1):
        A[0], A[i] = A[i], A[0]
        result.append(A.pop())
        min_heapify(A, 0)
    return result

def test():
    A = [16,4,10,14,7,9,3,2,8,1]
    min_heapify(A, 0)
    
    B = []

    # testeql(A, 0)  # fails, a single min_heapify does not sort the heap

    C = A[:]
    shuffle(C)
    build_min_heap(C)

    testeql(C, None)  # there are many max-heaps possible, must check manually
    
    D = [4,1,3,2,16,9,10,14,8,7]
    E = [16,14,10,8,7,9,3,2,4,1]
    build_min_heap(D)
    testeql(D,E)

    F = list(range(10))
    shuffle(F)
    print(F)
    testeql(heapsort(F), list(range(10)))
