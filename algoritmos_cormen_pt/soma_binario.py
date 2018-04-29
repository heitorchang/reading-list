# p. 16 Ex. 2.1-4
# soma de dois numeros binarios

a = [1, 0, 0, 1, 1]
b = [0, 1, 0, 1, 0]

c = [1, 0, 0, 0, 0]
d = [1, 0, 0, 0, 0]

def soma_place(a, b, carry):
    sum = a + b + carry
    if sum == 0:
        return (0, 0)
    elif sum == 1:
        return (1, 0)
    elif sum == 2:
        return (0, 1)
    else:
        return (1, 1)
        
def soma(a, b):
    # let a be longer
    if len(b) > len(a):
        a, b = b, a

    # fill b with zeros
    b = [0 for _ in range(len(a) - len(b))] + b
        
    result = [0 for _ in range(len(a))]
    carry = 0
    for place in range(len(a)-1, -1, -1):
        result[place], carry = soma_place(a[place], b[place], carry)
    if carry == 1:
        result = [carry] + result
    return result

def dec_to_bin(n):
    return list(map(int, list(bin(n)[2:])))

def binlst_to_dec(lst):
    return int(''.join(map(str, lst)), 2)
