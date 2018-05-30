# p. 394 Longest common subsequence

def lcs_length(x, y):
    m = len(x)
    n = len(y)
    b = [[None for _ in range(n+1)] for _ in range(m+1)]
    c = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:  # shift string indices
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = "\\"
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = "|"
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = "-"
    return c, b

def print_lcs(b, X, i, j, s):
    if i == 0 or j == 0:
        return s
    if b[i][j] == "\\":
        # recursion reverses order
        return print_lcs(b, X, i-1, j-1, X[i-1] + s)  
    elif b[i][j] == "|":
        return print_lcs(b, X, i-1, j, s)
    else:
        return print_lcs(b, X, i, j-1, s)

def lcs(x, y):
    c, b = lcs_length(x, y)
    return print_lcs(b, x, len(x), len(y), "")
    

def test():
    testeql(lcs("abcbdab", "bdcaba"), "bcba")
    testeql(lcs("ACCGGTCGAGTGCGCGGAAGCCGGCCGAA",
                "GTCGTTCGGAATGCCGTTGCTCTGTAAA"),
            "GTCGTCGGAAGCCGGCCGAA")
