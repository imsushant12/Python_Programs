"""
Find the element which occurs even number of times.
"""


def solve(a):
    d = dict()

    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for value in d:
        if d[value] % 2 == 0:
            return value

    return -1


if __name__ == "__main__":
    a = [1, 1, 2, 2, 3, 1]
    print(solve(a))
