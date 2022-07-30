def maximumRobberyRecursive(a, index):
    if index < len(a):
        if index == 0 and index + 2 == (len(a)):
            include = 0
            exclude = 0 + maximumRobberyRecursive(a, index + 1)
            return max(include, exclude)
        else:
            include = a[index] + maximumRobberyRecursive(a, index + 2)
            exclude = 0 + maximumRobberyRecursive(a, index + 1)
            return max(include, exclude)
    else:
        return 0


def maximumRobberyMemoisation(a, index, dp):
    if index < len(a):
        if dp[index] != -1:
            return dp[index]

        include = a[index] + maximumRobberyMemoisation(a, index+2, dp)
        exclude = 0 + maximumRobberyMemoisation(a, index+1, dp)
        dp[index] = max(include, exclude)
        return dp[index]
    else:
        return 0


def maximumRobberyTabulation(a):
    dp = [0] * (len(a) + 1)

    dp[0] = a[0]

    for i in range(1, len(a)):
        include = a[i] + dp[i - 2]
        exclude = 0 + dp[i - 1]
        dp[i] = max(include, exclude)

    return dp[len(dp) - 2]


if __name__ == "__main__":
    a = [1, 3, 2, 1]
    dp = [-1] * (len(a) + 1)

    answer = max(maximumRobberyMemoisation(a, 1, dp),
                 maximumRobberyMemoisation(a[:len(a)-1], 0, dp[:len(dp) - 1]))

    print("Maximum robbery possible: ", answer)
