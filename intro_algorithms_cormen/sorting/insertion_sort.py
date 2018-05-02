# p. 18

from random import shuffle

def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        # insert A[j] into the sorted sequence A[0:j-1]
        i = j - 1
        while i >= 0 and A[i] > key:
            # repeatedly shift values to the right
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key
    return A
    
def test():
    testeql(insertion_sort([3,1,2]), [1,2,3])
    testeql(insertion_sort([2,2,2]), [2,2,2])
    testeql(insertion_sort([3,-1,0,2,5,-6]), [-6,-1,0,2,3,5])

    # dynamic test
    L = list(range(10))
    shuffle(L)
    print("shuffled:", L)
    testeql(insertion_sort(L), list(range(10)))
