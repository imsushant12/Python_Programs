# Time Complexity: O(n!)

def count_paths(i, j, n, m):
    # base case
    if (i == n) or (j == m):
        return 0
    if (i == n - 1) and (j == m - 1):
        return 1

    # We can go in two directions:
    # 1. Rightwards
    # 2. Downwards
    rightwards = count_paths(i+1, j, n, m)
    downwards = count_paths(i, j+1, n, m)

    return rightwards + downwards


if __name__ == "__main__":
    i, j, n, m = (0, 0, 3, 3)
    print(count_paths(i, j, n, m))
