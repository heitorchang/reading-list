# p. 366

def bottom_up_cut_rod(p, n):
    r = [None] * (n + 1)  # r[0..n] is an empty array
    r[0] = 0

    for j in range(1, n+1):
        q = float('-inf')
        for i in range(1, j+1):
            q = max(q, p[i] + r[j-i])
        r[j] = q
    return r[n]


def optimal_first_piece(p, n):
    r = [None] * (n + 1)
    s = [None] * (n + 1)  # holds the optimal size i of the first piece to cut off

    r[0] = 0
    for j in range(1, n+1):
        q = float('-inf')
        for i in range(1, j+1):
            if q < p[i] + r[j-i]:
                q = p[i] + r[j-i]
                s[j] = i
        r[j] = q
    return r, s
    

def test():
    # p. 360
    p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    testeql(bottom_up_cut_rod(p, 4), 10)
    testeql(bottom_up_cut_rod(p, 7), 18)

    testeql(optimal_first_piece(p, 10),
            ([0,1,5,8,10,13,17,18,22,25,30],
             [None,1,2,3,2,2,6,1,2,3,10]))
