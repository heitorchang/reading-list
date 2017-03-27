# p. 145

bucket_sort = """
bucket_sort(A):

n = A.comprimento
seja B[0..n-1] um novo arranjo

for i = 0 to n-1
  faça B[i] uma lista vazia

for i = 1 to n
  insira A[i] na lista B[piso(n*A[i])]

for i = 0 to n-1
  ordene a lista B[i] com ordenacao por insercao

concatene as listas B[0], B[1], ..., B[n-1] em ordem
"""
