def maximumSumRecursive(a, index):
    if index < len(a):
        include = a[index] + maximumSumRecursive(a, index+2)
        exclude = 0 + maximumSumRecursive(a, index+1)
        return max(include, exclude)
    else:
        return 0


def maximumSumMemoisation(a, index, dp):
    if index < len(a):
        if dp[index] != -1:
            return dp[index]

        include = a[index] + maximumSumMemoisation(a, index+2, dp)
        exclude = 0 + maximumSumMemoisation(a, index+1, dp)
        dp[index] = max(include, exclude)
        return dp[index]
    else:
        return 0


def maximumSumTabulation(a):
    dp = [0] * (len(a) + 1)
   
    dp[0] = a[0]

    for i in range(1, len(a)):
        include = a[i] + dp[i - 2]
        exclude = 0 + dp[i - 1]
        dp[i] = max(include, exclude)

    return dp[len(dp) - 2]


def maximumSumSpaceOptimization(a):
    first = 0 
    second = a[0]  

    answer = 0 

    for i in range(1, len(a)):
        include = a[i] + first
        exclude = 0 + second
        answer = max(include, exclude)

        first = second
        second = answer

    return first


if __name__ == "__main__":
    a = [9, 9, 8, 2]
    dp = [-1] * (len(a) + 1)
    print("Maxim sum: ", maximumSumTabulation(a))
