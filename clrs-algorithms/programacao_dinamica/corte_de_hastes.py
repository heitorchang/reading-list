# p. 265

p = [0,10,50,80,90,100,170,170,200,240,300,320,29,30,39,36,35,41,43,49,50,52]

def cut_rod(p, n):
    if n == 0:
        return 0
    q = -1
    for i in range(1, n+1):
        q = max(q, p[i] + cut_rod(p, n-i))
    print("computed", n, 'as', q)
    return q

def memoized_cut_rod(p, n):
    r = [-1 for _ in range(n+1)]
    return memoized_cut_rod_aux(p, n, r)

def memoized_cut_rod_aux(p, n, r):
    # it appears that the reference to r (the memoization table)
    # is shared across recursive calls
    print('called', n, r, end=" ")
    if r[n] >= 0:
        print('returned',r[n])
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -1
        for i in range(1, n+1):
            print("\n\n  i", i)
            print("\n   max q",q,',', p[i], '+ ( call', n-i,'with r', r, ')')
            q = max(q, p[i] + memoized_cut_rod_aux(p, n-i, r))
        print("\nsaving", n, 'as', q)
        r[n] = q
    print(' returned q', q)
    return q

def bottom_up_cut_rod(prices, length):
    memo = [-1 for _ in range(length+1)]
    memo[0] = 0
    for trial_length in range(1, length+1):
        trial_value = -1
        for single_piece in range(1, trial_length+1):
            trial_value = max(trial_value, prices[single_piece] + memo[trial_length-single_piece])
        memo[trial_length] = trial_value
    return trial_value

def bottom_up_cut_rod_solution(prices, length):
    memo = [-1 for _ in range(length+1)]
    pieces = [0 for _ in range(length+1)]
    memo[0] = 0
    for trial_length in range(1, length+1):
        trial_value = -1
        cur_max = -1
        for single_piece in range(1, trial_length+1):
            trial_value = max(trial_value, prices[single_piece] + memo[trial_length - single_piece])
            if trial_value > cur_max:
                cur_max = trial_value
                cur_piece = single_piece
        memo[trial_length] = trial_value
        pieces[trial_length] = cur_piece
    # return trial_value
    return pieces

def optimal_price(prices, first_pieces, length):
    """first_pieces = bottom_up_cut_rod_solution(p, 10)"""
    if length == 0:
        return 0
    return prices[first_pieces[length]] + optimal_price(prices, first_pieces, length - first_pieces[length])
    
def pieces_prices(prices, pieces):
    result = [0]
    for i in range(1, len(pieces)):
        result.append(prices[pieces[i]] + result[i-1])
    return result
