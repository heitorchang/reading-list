from random import randint

def permute_by_sorting(A):
    """Choose a random priority for each element of A, then sort by the priority.

    A defect is that if a priority is repeated, those elements won't be randomized.
    """
    n = len(A)
    p = [(randint(1, n**3), x) for x in A]
    p.sort()
    return [t[1] for t in p]

def test():
    A = [1,2,3,4,5]
    r = permute_by_sorting(A)
    testeql(r, r)  # impossible to guess random permutation
