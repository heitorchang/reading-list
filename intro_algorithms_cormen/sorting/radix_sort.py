# p. 198

description = """
Radix sort depends on a stable sorting algorithm. First, the numbers are sorted by their ones column, then the tens column, hundreds, and so on. It is counterintuitive but works as long as the sorting is stable."""

def radix_sort(A, d):
    """Given that each element of A has d digits, where 1 is the lowest-order digit"""
    for i in range(1, d+1):
        # call a stable sort to sort A on digit i
        pass

def test():
    testeql(radix_sort([1,2,3], 1), None)
