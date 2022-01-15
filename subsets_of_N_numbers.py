def find_subsets(n, arr):
    # base cases
    if n == 0:
        print(arr)
        return

    # Adding the current N in the set
    arr.append(n)
    find_subsets(n-1, arr)

    # Not adding the current N in the set
    arr.pop()
    find_subsets(n-1, arr)

if __name__ == "__main__":
    n = 3
    arr = []
    answer = find_subsets(n, arr)
    print(answer)
