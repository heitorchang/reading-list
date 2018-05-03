# p. 31

from random import shuffle

def merge(A, p, q, r):
    """p <= q < r are indices of A.
    Assuming A[p..q] and A[q+1..r] are sorted, merge them into
    a single sorted subarray that replaces A[p..r]

    merge creates L and R, and overwrites A

    A = [1,2,3,5,6,7,9,11,15]
    i = [0,1,2,3,4,5,6, 7, 8]
    p = 1
    q = 3
    r = 8

    n1 = q - p + 1 = 3
    n2 = r - q = 5
    """

    # Split A[p..r] into L = A[p..q] and R = A[q+1..r]
    n1 = q - p + 1  # will hold A[p..q]
    n2 = r - q      # will hold A[q+1..r]

    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)
    
    for i in range(n1):
        L[i] = A[p+i]
    for j in range(n2):
        R[j] = A[q+j+1]

    # add sentinels
    L[n1] = float('inf')
    R[n2] = float('inf')

    # instead of sentinels, we can check if either L or R is empty,
    # and copy the non-empty subarray back into A. (p. 37, ex. 2.3-2)
    
    # indices of subarrays L and R (both already previously sorted)
    i = 0
    j = 0

    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort_subarray(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort_subarray(A, p, q)
        merge_sort_subarray(A, q+1, r)
        merge(A, p, q, r)

def merge_sort(A):
    merge_sort_subarray(A, 0, len(A)-1)
    return A
            
def test():
    A = [1,2,3,50,2,9,12]
    INF = float('inf')
    merge(A, 1, 3, 6)
    testeql(A, [1,2,2,3,9,12,50])

    testeql(merge_sort([3,1,2]), [1,2,3])
    testeql(merge_sort([-3,2,-1,0,INF]), [-3,-1,0,2,INF])

    L = list(range(10))
    shuffle(L)
    print("L", L)
    testeql(merge_sort(L), list(range(10)))
    
