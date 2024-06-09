"""Module providing a functions solving change set."""
def find_coins_greedy(amount):
    """Function implementing greedy algorithm to find coins."""
    coins = [50, 25, 10, 5, 2, 1]
    coin_count = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            coin_count[coin] = count
            amount -= coin * count
    return coin_count

def find_min_coins(amount):
    """Function implementing finding min amount of coins."""
    coins = [1, 2, 5, 10, 25, 50]
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    coin_count = [None] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_count[i] = coin

    if min_coins[amount] == float('inf'):
        return {}

    result = {}
    while amount > 0:
        coin = coin_count[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result

if __name__ == "__main__":

    amount = 113
    print(find_coins_greedy(amount))

    print(find_min_coins(amount))
