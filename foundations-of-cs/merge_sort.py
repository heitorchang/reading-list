# p. 77

from lst import Lst, build_Lst

def merge(lst1, lst2):
    if lst1 == None:
        return lst2
    elif lst2 == None:
        return lst1
    elif lst1.element <= lst2.element:
        lst1.next = merge(lst1.next, lst2)
        return lst1
    else:
        lst2.next = merge(lst1, lst2.next)
        return lst2

def test_merge():
    a = build_Lst([1,2,7,7,9])
    b = build_Lst([2,4,7,8])

    print(merge(a,b))

    c = None
    d = build_Lst([1])
    print(merge(c, d))
    
# p. 79 LIST split(LIST list)

# as a side effect, a becomes a list of odd-indexed elements of the original list. The return value of split is a list of even-indexed elements.
def split(lst):
    if lst == None:
        return None
    elif lst.next == None:
        return None
    else:
        pSecondCell = lst.next
        lst.next = pSecondCell.next
        pSecondCell.next = split(pSecondCell.next)
        return pSecondCell
    
def test_split():
    a = build_Lst([1,2,3,4,5])
    b = split(a)
    print(a)
    print(b)

    c = build_Lst([1,3,5,7,9,11])
    d = split(c)
    print(c)
    print(d)

# p. 81

def mergeSort(lst):
    if lst == None:
        return None
    elif lst.next == None:
        return lst
    else:
        secondLst = split(lst)
        return merge(mergeSort(lst), mergeSort(secondLst))

def test_mergeSort():
    a = build_Lst([3,9,2,4,5])
    s = mergeSort(a)
    print(s)
