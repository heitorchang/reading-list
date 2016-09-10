# p. 74 List of integers

# Linked list
# The empty list is None
class Lst:
    def __init__(self, element, next):
        self.element = element
        self.next = next

    def __str__(self):
        result = "("
        pointer = self
        while pointer != None:
            result += str(pointer.element) + " "
            pointer = pointer.next
        return result[:-1] + ")"  # display in Lisp style

def build_Lst(arr):
    arr = arr[::-1]
    result = Lst(arr[0], None)
    for elem in arr[1:]:
        result = Lst(elem, result)
    return result        

# p. 83
def recBuild_Lst(arr):
    if len(arr) == 0:
        return None
    else:
        pNewCell = Lst(arr[0], recBuild_Lst(arr[1:]))
        return pNewCell
    
