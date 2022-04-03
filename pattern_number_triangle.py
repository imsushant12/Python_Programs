"""
Problem:
--------
1
2 3
3 4 5
4 5 6 7
5 6 7 8 9
6 7 8 9 10 11
"""


def solve_extra_variable(n):
    row = 1
    current_value = 0
    column = 0

    while row <= n:
        column = 1
        current_value = row

        while column <= row:
            print(current_value, end=' ')
            current_value += 1
            column += 1
        print()
        row += 1


def solve(n):
    row = 1

    while row <= n:
        column = row
        while column <= ((row * 2) - 1):
            print(column, end=' ')
            column += 1
        print()
        row += 1


if __name__ == '__main__':
    n = int(input())
    solve(n)
