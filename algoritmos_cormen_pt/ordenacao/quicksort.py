from random import randint

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quicksort_step(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort_step(A, p, q-1)
        quicksort_step(A, q+1, r)

def quicksort(A):
    quicksort_step(A, 0, len(A)-1)

# p. 130

def randomized_partition(A, p, r):
    i = randint(p, r)
    A[p], A[i] = A[i], A[p]
    return partition(A, p, r)

def randomized_quicksort_step(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)
        randomized_quicksort_step(A, p, q-1)
        randomized_quicksort_step(A, q+1, r)

def randomized_quicksort(A):
    randomized_quicksort_step(A, 0, len(A)-1)
