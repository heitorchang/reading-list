# Quick.java

from random import shuffle

def quicksort(a):
    shuffle(a)

    qsorthelper(a, 0, len(a) - 1)


def qsorthelper(a, lo, hi):
    if lo >= hi:
        return
    j = partition(a, lo, hi)
    qsorthelper(a, lo, j-1)
    qsorthelper(a, j+1, hi)


def partition(a, lo, hi):
    i = lo
    j = hi + 1
    v = a[lo]

    while True:
        while a[i] < v:
            if i == hi:
                break
            i += 1

        while v < a[j]:
            if j == lo:
                break
            j -= 1

        if i >= j:
            break

        a[i], a[j] = a[j], a[i]

    a[lo], a[j] = a[j], a[lo]

    # now, a[lo ... j-1] <= a[j] <= a[j+1 ... hi]
    return j
