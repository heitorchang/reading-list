def convBase(n, base):
    convStr = "0123456789ABCDEF"
    if n < base:
        return convStr[n]
    else:
        return convBase(n // base, base) + convStr[n % base]

test(convBase(1453, 16), "5AD")
