# Poor man's quicksort

def pmqsort(a):
    qsorthelper(a, 0, len(a) - 1)


def qsorthelper(a, lo, hi):
    j = partition(a, lo, hi)
    left = qsorthelper(a, lo, j-1)
    right = qsorthelper(a, j+1, hi)
