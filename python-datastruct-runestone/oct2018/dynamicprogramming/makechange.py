# 4.12

def dpMakeChange(coinValueList, change):
    minCoins = [0] * (change+1)

    for cents in range(change+1):
        coinCount = cents
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j] + 1
        minCoins[cents] = coinCount
    print(minCoins)
    return minCoins[change]

# test(dpMakeChange([1,5,10,21,25], 63), 3)


def dpMakeChangeCoinsUsed(coinValueList, change):
    minCoins = [0] * (change+1)
    coinsUsed = [0] * (change+1)

    for cents in range(change+1):
        coinCount = cents
        newCoin = 1

        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin

    print(coinsUsed)
    return minCoins[change]


test(dpMakeChangeCoinsUsed([1,5,10,21,25], 63), 3)
