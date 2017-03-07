def merge_step(a, b, result):
    if len(a) == 0:
        return result + b
    if len(b) == 0:
        return result + a
    if a[0] < b[0]:
        return merge_step(a[1:], b, result + [a[0]])
    else:
        return merge_step(a, b[1:], result + [b[0]])

def merge(a, b):
    return merge_step(a, b, [])
    
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        midpt = len(arr) // 2
        left = arr[:midpt]
        right = arr[midpt:]
        return merge(merge_sort(left), merge_sort(right))
