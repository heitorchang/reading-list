from random import randint

def randomize_in_place(A):
    n = len(A)
    for i in range(n):
        r = randint(i, n-1)
        A[i], A[r] = A[r], A[i]


def test():
    L = [1,2,3,4,5]
    randomize_in_place(L)
    testeql(L, L)  # impossible to guess random permutation
