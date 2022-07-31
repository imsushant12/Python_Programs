def cutSegmentsRecursive(n, xyz):
    if n == 0:
        return 0
    if n < 0:
        return -99999

    # we need to add `1` to all the results as we are cutting so current value is also added.
    x = cutSegmentsRecursive(n-xyz[0], xyz) + 1
    y = cutSegmentsRecursive(n-xyz[1], xyz) + 1
    z = cutSegmentsRecursive(n-xyz[2], xyz) + 1

    answer = max(x, y, z)

    return answer




def cutSegmentsMemoization(n, xyz, dp):
    if n == 0:
        return 0
    if n < 0:
        return -99999

    # adding dp check.
    if dp[n] != -1:
        return dp[n]

    # we need to add `1` to all the results as we are cutting so current value is also added.
    x = cutSegmentsMemoization(n-xyz[0], xyz, dp) + 1
    y = cutSegmentsMemoization(n-xyz[1], xyz, dp) + 1
    z = cutSegmentsMemoization(n-xyz[2], xyz, dp) + 1

    dp[n] = max(x, y, z)

    return dp[n]




def cutSegmentsTabulation(n, xyz):
    dp = [-99999] * (n+1)

    # adding the base value.
    dp[0] = 0

    for i in range(1, n+1):
        if (i - xyz[0]) >= 0:
            dp[i] = max(dp[i], dp[i-xyz[0]] + 1)
        if (i - xyz[1]) >= 0:
            dp[i] = max(dp[i], dp[i-xyz[1]] + 1)
        if (i - xyz[2]) >= 0:
            dp[i] = max(dp[i], dp[i-xyz[2]] + 1)

    return dp[n]




if __name__ == "__main__":
    n = 7
    xyz = [5, 2, 2]
    dp = [-1] * (n+1)

    answer = cutSegmentsTabulation(n, xyz)
    if answer < 0:
        print("We cannot cut the rod using the values of x, y, or z!")
    else:
        print("Maximum possible ways to cut the rod is: ", answer)
