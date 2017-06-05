def binarySearch(x, lst):
    i = 0
    j = len(lst)

    while i < j:
        m = (i + j) // 2
        if lst[m] == x:
            return m
        elif lst[m] > x:
            j = m
        else:
            i = m + 1
    return -1
        
        

    print(lst[i:m], lst[m:j])

def test():
    testeql(binarySearch(2, [1,2,3,4,5,6]), 1)
    testeql(binarySearch(1, [0,1]), 1)
    testeql(binarySearch(5, [0, 1,2,3,4,5,6,7]), 5)
    testeql(binarySearch(5, [0, 1,2,3,4,5,6,7,8]), 5)
    testeql(binarySearch(9, [0,1,2]), -1)
