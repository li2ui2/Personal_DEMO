def coinChange(coins, amount):
    n = len(coins)
    if amount == 0 or n == 0:
        return -1
    if n == 1 and coins[0] < amount:
        return -1

    dp = [float("inf") for _ in range(amount + 1)]
    for coin in coins:
        dp[coin] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    if dp[amount] == -1:
        return -1
    return dp[-1]


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    print(coinChange(coins, amount))
