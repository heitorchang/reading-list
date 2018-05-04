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
    if high == low:                              # 1
        return (low, high, A[low])               # 2
    else:
        mid = (low + high) // 2                  # 3 
        left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)                # 4
        right_low, right_high, right_sum = find_maximum_subarray(A, mid+1, high)          # 5
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)  # 6
        if left_sum >= right_sum and left_sum >= cross_sum:     # 7
            return (left_low, left_high, left_sum)              # 8
        elif right_sum >= left_sum and right_sum >= cross_sum:  # 9
            return (right_low, right_high, right_sum)           # 10
        else:
            return (cross_low, cross_high, cross_sum)           # 11

def main(A):
    return find_maximum_subarray(A, 0, len(A)-1)


def max_subarray_415_fail(A):
    # p. 75 ex. 4.1-5
    """Starting on the left, progress to the right"""
    max_left = max_right = 0
    max_sum = float('-inf')
    for ptr in range(1, len(A)):
        sum_add_right = sum(A[max_left:ptr])
        print(max_left, ptr, sum_add_right)
    return (max_left, max_right, max_sum)
    

def max_subarray_rutgers(A):
    max_sum = float('-inf')
    low = high = 0
    running_sum = 0
    running_low = 1
    for i in range(len(A)):
        running_sum += A[i]
        if running_sum > max_sum:
            low = running_low
            high = i
            max_sum = running_sum
        if running_sum < 0:
            running_sum = 0
            running_low = i + 1
    return (low, high, max_sum)
    
def test():
    A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
    B = [0,1,-5,3,4,-2,-1,7,-9]
    C = [-1,-1,-1,3,-1,-1,-1]
    D = [-3,-1,-2]
    
    testeql(find_max_crossing_subarray(B, 0, 3, 8), (3,7,11))

    # midpoint (point after A[mid]) must be crossed, so the max_subarray contains two elements
    testeql(find_max_crossing_subarray(C, 0, 3, 6), (3,4,2))

    testeql(main(A), (7, 10, 18+20-7+12))

    testeql(main(D), (1, 1, -1))

    # testeql(max_subarray_415(A), (7, 10, 43))

    testeql(max_subarray_rutgers(A), (7, 10, 43))

