# p. 40

description = """Repeatedly swap adjacent elements that are out of order"""

def bubblesort(A):
    for i in range(len(A)):
        for j in range(len(A)-1, i, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
    return A


def test():
    # tests from merge_sort
    INF = float('inf')
    testeql(bubblesort([3,1,2]), [1,2,3])
    testeql(bubblesort([-3,2,-1,0,INF]), [-3,-1,0,2,INF])

    L = list(range(10))
    shuffle(L)
    print("L", L)
    testeql(bubblesort(L), list(range(10)))
    

