# p. 171

from random import shuffle

def quicksort_step(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort_step(A, p, q-1)
        quicksort_step(A, q+1, r)

def quicksort(A):
    quicksort_step(A, 0, len(A)-1)
    return A

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1
    
def test():
    A = [1,2,3,50,2,9,12]
    INF = float('inf')

    testeql(quicksort([3,1,2]), [1,2,3])
    testeql(quicksort([-3,2,-1,0,INF]), [-3,-1,0,2,INF])

    L = list(range(10))
    shuffle(L)
    print("L", L)
    testeql(quicksort(L), list(range(10)))
    

