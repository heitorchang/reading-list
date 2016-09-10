# p. 33 Iteration

# sorts in-place

def selection_sort(arr):
    n = len(arr)
    for i in range(0, n-1):
        small = i
        for j in range(i+1, n):
            if arr[j] < arr[small]:
                small = j
        temp = arr[small]
        arr[small] = arr[i]
        arr[i] = temp;
