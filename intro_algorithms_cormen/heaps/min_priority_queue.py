# p. 163

from min_heap import min_heapify, build_min_heap

def heap_minimum(A):
    return A[0]

def heap_extract_min(A):
    """Removes and returns the element with the smallest key"""
    min = A[0]
    A[0] = A.pop()
    min_heapify(A, 0)
    return min

def heap_decrease_key(A, i, key):
    if key > A[i]:
        raise ValueError("New key is greater than current key")
    A[i] = key
    while i > 0 and A[parent(i)] > A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)

def min_heap_insert(A, key):
    A.append(float('inf'))
    heap_decrease_key(A, len(A) - 1, key)

def test():
    A = [3,1,14,7,9,2,4,8,10]
    build_min_heap(A)
    heap_extract_min(A)
    heap_decrease_key(A, 7, -1)
    min_heap_insert(A, -.2)
    print(A)
