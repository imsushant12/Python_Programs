
def count_set_bits(n):
    counter = 0

    while n != 0:
        bit = n & 1
        if bit == 1:
            counter += 1
        n = n >> 1

    return counter


if __name__ == '__main__':
    a = int(input())
    b = int(input())

    answer = count_set_bits(a) + count_set_bits(b)
    print(answer)
