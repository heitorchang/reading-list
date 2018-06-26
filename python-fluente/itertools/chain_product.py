# create a sequence [(a,a,a,1,1,1), (a,a,b,1,1,2),...]

def main():
    ltrs = product('abc', repeat=3)
    nums = product(range(1, 4), repeat=3)
    zipped = zip(ltrs, nums)
    ans = map(lambda x: tuple(chain(*x)), zipped)
    
    return list(islice(ans, 10))

test(main(), None)
