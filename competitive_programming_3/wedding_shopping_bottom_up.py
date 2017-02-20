M = 20 # starting money
C = 3  # number of garments

# price = table of prices for each garment and model
price = [[6,4,8],
         [5,10],
         [1,5,3,5]]

reachable = [[0] * M for _ in range(C)]

def print_reachable():
    for row in reachable:
        print(row)

current_row = 0

for p in price[0]:
    reachable[0][M-p] = 1

for g in range(C):
    for money in range(M):
        if reachable[g-1][money] > 0:
            for k in price[g]:
                if money - k >= 0:
                    reachable[g][money - k] = 1

# C code
# for (money = 0; money <= M && !reachable[C - 1][money]; money++);
# if (money == M+1) printf("No solution")
# else printf("%d", M - money)
