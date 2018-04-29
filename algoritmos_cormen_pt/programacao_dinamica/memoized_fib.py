def naive_fib(n):
    if n < 2:
        return 1
    else:
        val = naive_fib(n-1) + naive_fib(n-2)
        print(" "*n, n, val)
        return val
    # slow at n = 30

def memo_fib(n):
    memo = [-1 for _ in range(n+1)]

    # base cases
    memo[0] = 1
    memo[1] = 1
    
    return memo_fib_aux(n, memo)

def memo_fib_aux(n, memo):
    print(" "*n, n, memo)
    if memo[n] >= 0:
        print("\n  retrieving", n, "as", memo[n], '\n')
        return memo[n]
    else:
        memo[n] = memo_fib_aux(n-1, memo) + memo_fib_aux(n-2, memo)
        print("\nmemoizing", n, "as", memo[n], "\n")
        return memo[n]
