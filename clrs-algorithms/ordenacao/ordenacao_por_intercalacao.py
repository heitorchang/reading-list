def intercalar(A, p, q, r):
    """Considera que A[p..q] e A[q+1..r] estao ordenados"""

    # print("intercalar:", p, q, r) 
    n1 = q - p + 1  # comprimento de A[p..q], nao é afetado por 
    n2 = r - q      # arranjos comecarem com 0 
    L = [0 for _ in range(n1+1)]
    R = [0 for _ in range(n2+1)]
    
    for i in range(n1):
        L[i] = A[p+i]
    for j in range(n2):
        R[j] = A[q+j+1]
        
    L[n1] = float('inf')
    R[n2] = float('inf')

    # print("L", L)
    # print("R", R)
    
    i = 0  # arranjos em Python comecam com 0 
    j = 0
    
    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return A

def my_test():
    #    0     2  3  4  5  6  7  8  9 10 11 12 13
    A = [0, 0, 0, 2, 4, 5, 7, 1, 2, 3, 6, 0, 0, 0]

    # OBS: q é o índice do último elemento de L (Left) 
    return intercalar(A, 3, 6, 10)

def my_test_b():
    B = [0, 0, 2, 7, 9, 1, 1, 3, 5, 9, 11, 12, 0, 0]
    return intercalar(B, 2, 4, 11)

def ordenar_por_intercalacao_passo(A, p, r):
    if p < r:
        q = (p + r) // 2
        # print("q", q) 
        ordenar_por_intercalacao_passo(A, p, q)
        ordenar_por_intercalacao_passo(A, q+1, r)
        intercalar(A, p, q, r) 

def ordenar_por_intercalacao(A):
    ordenar_por_intercalacao_passo(A, 0, len(A) - 1) 
