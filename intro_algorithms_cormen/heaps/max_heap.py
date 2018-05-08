# p. 154

from heap import left, right, parent
from random import shuffle

def max_heapify(A, i):
    """Given array A and index i, max_heapify assumes left(i) and right(i) are max-heaps, but A[i] might be smaller than its children."""

    L = left(i)
    R = right(i)

    if L <= len(A) - 1 and A[L] > A[i]:  # assume len(A) is A.heap_size
        largest = L
    else:
        largest = i

    if R <= len(A) - 1 and A[R] > A[largest]:
        largest = R
        
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)

def build_max_heap(A):
    for i in range((len(A) // 2) - 1, -1, -1):
        max_heapify(A, i)


def heapsort(A):
    """p. 160, using a new array for the result"""
    result = []
    build_max_heap(A)
    print(A)
    for i in range(len(A) - 1, -1, -1):
        A[0], A[i] = A[i], A[0]
        result.append(A.pop())
        max_heapify(A, 0)
    return result[::-1]

def test():
    A = [16,4,10,14,7,9,3,2,8,1]
    max_heapify(A, 1)
    
    B = [16,14,10,8,7,9,3,2,4,1]

    testeql(A, B)

    C = A[:]
    shuffle(C)
    build_max_heap(C)

    # testeql(C, C)  # there are many max-heaps possible, must check manually
    
    D = [4,1,3,2,16,9,10,14,8,7]
    E = [16,14,10,8,7,9,3,2,4,1]
    build_max_heap(D)
    testeql(D,E)

    F = list(range(10))
    shuffle(F)
    print(F)
    testeql(heapsort(F), list(range(10)))
