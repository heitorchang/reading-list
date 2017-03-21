# p. 93

from random import randint

def randomize_in_place(lst):
    A = lst[:]
    n = len(A)
    for j in range(n):
        # note: random range is from j to end, not 0 to end
        r = randint(j, n-1)  
        A[j], A[r] = A[r], A[j]
    return A
