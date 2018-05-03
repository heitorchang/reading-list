# p. 39 ex. 2.3-7

description = """
Describe an O(n lg n)-time algorithm that, given a set S of n integers
and another integer x, determines whether or not there exist two
elements in S whose sum is exactly x.
"""

def sum_exists_brute(s, x):
    """Idea: looking for a + b = x, where a and b are in s.
    Instead, we look for an a = x - b, if a is in s, excluding b itself.

    But this is an O(n^2) algorithm
    """
    
    d = [x - b for b in s]  # differences
    for i, a in enumerate(d):  # check each value
        if a in s[i+1:]:
            return True
    return False

def sum_exists(s, x):
    # Hash version
    # https://stackoverflow.com/questions/4720271/find-a-pair-of-elements-from-an-array-whose-sum-equals-a-given-number

    # build hash
    h = {}
    for i, n in enumerate(s):
        h[n] = i  # key is the element, and value is index

    # iterate
    for i, n in enumerate(s):
        if h.get(x - n, i) != i:  # if there are duplicates, the "right"
                                  # pair will have a different index
            return True
    return False
        
def test():
    testeql(sum_exists([1,2,3], 4), True)
    testeql(sum_exists([9,20,10], 1), False)
    testeql(sum_exists([3,3], 6), True)
    testeql(sum_exists([3,2], 6), False)
    testeql(sum_exists([6,1], 6), False)
