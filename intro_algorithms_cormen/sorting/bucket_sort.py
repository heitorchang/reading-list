# p. 201

import itertools

description = """
Bucket sort assumes an uniform distribution of elements in the array A.
For each element of A, insert it into its corresponding bucket; for example, 0.21 goes in the [0.2, 0.3) bucket. Then use insertion sort for each bucket"""

def bucket_sort(A):
    """Assuming elements of A are floats in the range [0,1)"""
    B = [0] * len(A)
    n = len(A)
    for i in range(n):
        # make B[i] an empty list
        B[i] = list()
    for i in range(n):
        B[floor(n * A[i])].append(A[i])
    for i in range(n):
        B[i].sort()
    return list(itertools.chain.from_iterable(B))

def test():
    testeql(bucket_sort([0.3, 0.1, 0.2, 0.4, 0.5, 0.9]), [0.1,0.2,0.3,0.4,0.5,0.9])
        
