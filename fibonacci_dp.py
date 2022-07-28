# Top-Down Approach
# Time Complexity : O(n)
# Space Complexity : O(n) + O(n) == O(n), extra O(n) for the recursive call stack.
def fibonacciMemorization(n, dp):
    # handling the base case.
    if n <= 1:
        return n

    # checking if the current value is already encountered or not.
    if dp[n] != -1:
        return dp[n]

    # recursively getting down to smaller values of n.
    dp[n] = fibonacciMemorization(n-1, dp) + fibonacciMemorization(n-2, dp)
    return dp[n]


# Bottom-Up Approach
# Time Complexity : O(n)
# Space Complexity : O(n)
def fibonacciTabulation(n):
    dp = []

    # adding base case-values.
    dp.append(0)
    dp.append(1)

    # filling up the dp array.
    for i in range(2, n+1):
        value = dp[i-1] + dp[i-2]
        dp.append(value)

    return dp[n]


if __name__ == "__main__":
    n = 7
    dp = [-1] * (n+1)

    print(f"{n}th fibonacci term is:", fibonacciMemorization(n, dp))
