import loop

def counting_sort(A):
    A = [0] + A[:]  # make A 1-indexed
    k = max(A)
    len_A = len(A) - 1
    B = [0 for _ in range(len_A+1)]
    C = [0 for _ in range(k+1)]
    
    for j in loop.to(1, len_A):
        C[A[j]] += 1
        
    for i in range(1, k+1):
        C[i] += C[i-1]
        
    for j in loop.downto(len_A, 1):
        print(j, A[j], C[A[j]])
        B[C[A[j]]] = A[j]
        C[A[j]] -= 1
        
    return B[1:]
