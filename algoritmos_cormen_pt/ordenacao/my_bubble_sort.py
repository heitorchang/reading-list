from copy import deepcopy

def my_bubble_sort(in_arr):
    arr = deepcopy(in_arr)
    len_arr = len(arr)
    for i in range(len(arr) - 1):
        for j in range(i, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
