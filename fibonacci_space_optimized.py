# Time Complexity : O(n)
# Space Complexity : O(1)
def fibonacciOptimized(n):
    # handling base case.
    if n <= 1:
        return n

    # initially adding the base values.
    first = 0
    second = 1

    currentNumber = 0
    for i in range(2, n+1):
        currentNumber = first + second
        first = second
        second = currentNumber

    return currentNumber


if __name__ == "__main__":
    n = 6
    print(f"{n}th fibonacci term is:", fibonacciOptimized(n))
