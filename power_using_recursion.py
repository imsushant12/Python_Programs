def find_power(x, y):
    # base cases.
    if y == 0:
        return 1
    if y == 1:
        return x

    # recursive calls.
    if (y % 2 == 0):        # Even number case.
        return (find_power(x, y//2) * find_power(x, y//2))
    else:                   # Odd number case.
        return (x * find_power(x, y//2) * find_power(x, y//2))


if __name__ == "__main__":
    x = 2
    y = 5

    print(find_power(x, y))
