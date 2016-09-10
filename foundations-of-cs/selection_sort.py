# p. 33 Iteration

# sorts in-place
# first define an array a, by, for example, a = [1, 3, 2]
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

# p. 73 recursive

def recSS(arr, i):  # call with i = 0
    n = len(arr)
    if i < n-1:
        small = i
        for j in range(i+1, n):
            if arr[j] < arr[small]:
                small = j
        temp = arr[small]
        arr[small] = arr[i]
        arr[i] = temp
        recSS(arr, i+1)

