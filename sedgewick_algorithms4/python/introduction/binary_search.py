# p. 25
# recursive implementation of binary search

def search(key, a):
    return rank(key, a, 0, len(a) - 1)


def rank(key, a, lo, hi):
    if (lo > hi):
        return -1
    mid = lo + (hi - lo) // 2
    if key < a[mid]:
        return rank(key, a, lo, mid - 1)
    elif key > a[mid]:
        return rank(key, a, mid + 1, hi)
    else:
        return mid
    
        
pairtest(search(3, [1, 3]), 1,
         search(9, [1, 2, 3]), -1,
         search(5, [1, 2, 3, 4, 5]), 4)
