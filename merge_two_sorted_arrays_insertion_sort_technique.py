# Time complexity: O(n log(n)) + O(n) = O(n log n).
# n log(n) for sorting the second array.
# O(n) for traversing the array.

def mergeArrays(a1, a2):
    for i in range(len(a1)):
        if a1[i] > a2[0]:
            a1[i], a2[0] = a2[0], a1[i]
            a2.sort()


if __name__ == '__main__':
    a1 = [1, 4, 7, 8, 10]
    a2 = [2, 3, 9]

    mergeArrays(a1, a2)
    print(a1)
    print(a2)