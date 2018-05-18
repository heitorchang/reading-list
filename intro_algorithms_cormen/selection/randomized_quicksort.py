# p. 216

from random import shuffle, randint

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

def randomized_partition(A, p, r):
    # p. 179
    """By randomizing the pivot, we expect the split of the input array to be reasonably well balanced"""
    i = randint(p, r)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)

def randomized_select(A, p, r, i):
    # p. 216
    if p == r:
        return A[p]
    q = randomized_partition(A, p, r)
    k = q - p + 1
    if (i+1) == k:  # the pivot value is the answer
        return A[q]
    elif i < k:
        return randomized_select(A, p, q-1, i)
    else:
        return randomized_select(A, q+1, r, i-k)

def test():
    L = [1,3,5,7,9]
    shuffle(L)
    print("L", L)
    testeql(randomized_select(L, 0, len(L)-1, 0), 1)
    testeql(randomized_select(L, 0, len(L)-1, 1), 3)
    testeql(randomized_select(L, 0, len(L)-1, 2), 5)
    testeql(randomized_select(L, 0, len(L)-1, 3), 7)
    testeql(randomized_select(L, 0, len(L)-1, 4), 9)
    
