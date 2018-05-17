# p. 171

# the worst-case scenario occurs when the array is already sorted, or in reverse order

from random import shuffle, randint

STEPS = 0

def quicksort_step(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort_step(A, p, q-1)
        quicksort_step(A, q+1, r)

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

def randomized_quicksort(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)
        randomized_quicksort(A, p, q-1)
        randomized_quicksort(A, q+1, r)

def quicksort(A):
    randomized_quicksort(A, 0, len(A)-1)
    return A
        
def test():
    A = [1,2,3,50,2,9,12]
    INF = float('inf')

    testeql(quicksort([3,1,2]), [1,2,3])
    testeql(quicksort([-3,2,-1,0,INF]), [-3,-1,0,2,INF])

    L = list(range(10))
    shuffle(L)
    print("L", L)
    testeql(quicksort(L), list(range(10)))
    

SORTED = [1,2,3,4,5,6,7,8,9]
REVERSED = [9,8,7,6,5,4,3,2,1]
RANDOM = [3, 2, 4, 1, 5, 9, 6, 8, 7]

def steps(A, p, r):
    global STEPS
    if p < r:
        q = partition(A, p, r)
        steps(A, p, q-1)
        steps(A, q+1, r)
        STEPS += 1

# steps(SORTED, 0, len(SORTED)-1)  # 8
# steps(REVERSED, 0, len(REVERSED)-1)  # 8
steps(RANDOM, 0, len(RANDOM)-1)  # 6
