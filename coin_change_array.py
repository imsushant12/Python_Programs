def coinChangingWays(n, a, index):
    if n == 0:
        return 1
    if n < 0 or index >= len(a):
        return 0

    answer1 = coinChangingWays(n-a[index], a, index)
    answer2 = coinChangingWays(n, a, index+1)
    return (answer1+answer2)


if __name__ == "__main__":
    n = 4
    a = [1, 2, 3]
    index = 0
    answer = coinChangingWays(n, a, index)
    print("Number of ways to get the change: ", answer)
