"""
Problem Statement:
------------------
Consider a rat placed at (0, 0) in a square matrix of order N * N. It has to reach the destination at (N - 1, N - 1). Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel through it.
Note: In a path, no cell can be visited more than one time. If the source cell is 0, the rat cannot move to any other cell.

Example 1:
----------
Input:
N = 4
m[][] = {{1, 0, 0, 0},
         {1, 1, 0, 1},
         {1, 1, 0, 0},
         {0, 1, 1, 1}}

Output: DDRDRR DRDDRR

Explanation: The rat can reach the destination at (3, 3) from (0, 0) by two paths - DRDDRR and DDRDRR, when printed in sorted order we get DDRDRR DRDDRR.
"""


def isSafe(x, y, m, n, visited):
    if x >= 0 and x < n and y >= 0 and y < n and m[x][y] == 1 and visited[x][y] == 0:
        return True
    else:
        return False


def findPathHelper(m, n, x, y, visited, path, answer):
    if x == (n - 1) and y == (n - 1):
        answer.append("".join(path))
        return

    # marking the current place as visited
    visited[x][y] = 1
    if isSafe(x+1, y, m, n, visited):
        path.append("D")
        findPathHelper(m, n, x+1, y, visited, path, answer)
        # backtrack
        path.pop()

    if isSafe(x, y-1, m, n, visited):
        path.append("L")
        findPathHelper(m, n, x, y-1, visited, path, answer)
        # backtrack
        path.pop()

    if isSafe(x, y+1, m, n, visited):
        path.append("R")
        findPathHelper(m, n, x, y+1, visited, path, answer)
        # backtrack
        path.pop()

    if isSafe(x-1, y, m, n, visited):
        path.append("U")
        findPathHelper(m, n, x-1, y, visited, path, answer)
        # backtrack
        path.pop()

    visited[x][y] = 0


def findPath(m, n):
    # handling the base case.
    if m[0][0] == 0:
        return []

    visited = [[0 for j in range(n)] for i in range(n)]
    x = 0
    y = 0
    answer = []
    path = []
    findPathHelper(m, n, x, y, visited, path, answer)
    print(answer)


if __name__ == "__main__":
    maze = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
    n = 4

    findPath(maze, n)
