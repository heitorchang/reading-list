# p. 195

from random import shuffle

def counting_sort_process(A, B, k):
    """Sort A into B"""
    C = [0] * (k+1)
    for i in range(k+1):
        C[i] = 0  # redundant but keeping this line of original code
    for j in range(len(A)):
        C[A[j]] += 1
    # C[i] now contains the number of elements equal to i
    for i in range(1, k+1):
        C[i] += C[i-1]
    # C[i] now contains the number of elements less than or equal to i
    for j in range(len(A)-1, -1, -1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1
    return B

def counting_sort(A):
    return counting_sort_process(A, [0] * len(A), int(max(A)))

def test():
    A = [1,2,3,50,2,9,12]

    testeql(counting_sort([3,1,2]), [1,2,3])
    testeql(counting_sort([3,2,1,0,3,8]), [0, 1, 2, 3, 3, 8])

    L = list(range(10))
    shuffle(L)
    print("L", L)
    testeql(counting_sort(L), list(range(10)))
