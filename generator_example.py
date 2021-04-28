#generator to generate table of 3
def table(n):
    i = 0
    while n:
        n -= 1
        i = i+1
        yield i*3

ls = []
it = table(10)

while True:
    try:
        ls.append(next(it))
    except StopIteration:
        break

print(ls)