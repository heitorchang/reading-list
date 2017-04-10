def one_indexed(A):
    # NOT VERY USEFUL, BECAUSE OPERATIONS LIKE MAX WORK ON KEYS
    result = {}
    
    for index, elem in enumerate(A):
        result[index+1] = elem
    return result
