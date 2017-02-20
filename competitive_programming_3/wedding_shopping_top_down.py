from itertools import repeat
from functools import reduce

M = 20 # starting money
C = 3  # number of garments (belts, shirts, shoes)

# price = table of prices for each garment and model
price = [[6,4,8],
         [5,10],
         [1,5,3,5]]

# memo = Dynamic Programming table
memo = [[-1] * C for _ in range(M+1)]

def shop(money, g):
    if money < 0:
        return -1000
    if g == C:
        return M - money
    if memo[money][g] != -1:
        return memo[money][g]
    ans = -1
    for p in price[g]:
        ans = max(ans, shop(money - p, g+1))
    memo[money][g] = ans
    return memo[money][g]
