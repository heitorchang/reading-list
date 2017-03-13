# p. 18

def insertion_sort(A):  # ordena no lugar
    # nota: no livro, A = [1...n]
    # for j = 2 to comprimento -> for j in range(1, comprimento)
    # while i > 0 ... -> while i >= 0
    comprimento = len(A)
    for j in range(1, comprimento):
        chave = A[j]
        i = j - 1
        while i >= 0 and A[i] > chave:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = chave

def my_insertion_sort(A):
    result = []
    for A_elem in A:
        insert_inx = 0
        for result_elem in result:
            if result_elem < A_elem:
                insert_inx += 1
        result.insert(insert_inx, A_elem)
    return result
