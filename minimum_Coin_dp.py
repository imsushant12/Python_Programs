def minimumCoinsRecursive(coins, money,  answer):
    if money == 0:
        return 1

    if money < 0:
        return 0

    for i in range(len(coins)):
        currentAnswer = minimumCoinsRecursive(coins, money - coins[i], answer)
        if currentAnswer != -1:
            answer = min(answer, 1 + currentAnswer)
    return answer


def minimumCoinsMemorization(coins, money, answer, dp):
    if money == 0:
        return 1
    if money < 0:
        return 0

    if dp[money] != -1:
        return dp[money]

    for i in range(len(coins)):
        currentAnswer = minimumCoinsMemorization(
            coins, money - coins[i], answer, dp)
        if currentAnswer != -1:
            dp[money] = min(answer, 1 + currentAnswer)

    return dp[money]


if __name__ == "__main__":
    coins = [1, 2, 3]
    money = 7
    answer = 9999999
    dp = [-1] * (money + 1)
    print(minimumCoinsMemorization(coins, money, answer, dp))
