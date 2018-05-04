def find_max_crossing_subarray(A, low, mid, high):
    """Find the endpoints of the maximum subarray of A and its sum, provided that it crosses the midpoint mid.
    """

    sum = 0
    left_sum = float('-inf')
    max_left = mid

    for i in range(mid, low-1, -1):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    sum = 0
    right_sum = float('-inf')
    max_right = mid+1
    
    for j in range(mid+1, high+1):
        sum += A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return (max_left, max_right, left_sum+right_sum)

def find_maximum_subarray(A, low, high):
    if high == low:
        return (low, high, A[low])
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(A, mid+1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)

def main(A):
    return find_maximum_subarray(A, 0, len(A)-1)
    
def test():
    A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
    B = [0,1,-5,3,4,-2,-1,7,-9]
    C = [-1,-1,-1,3,-1,-1,-1]
    
    testeql(find_max_crossing_subarray(B, 0, 3, 8), (3,7,11))

    # midpoint (point after A[mid]) must be crossed, so the max_subarray contains two elements
    testeql(find_max_crossing_subarray(C, 0, 3, 6), (3,4,2))

    testeql(main(A), (7, 10, 18+20-7+12))
