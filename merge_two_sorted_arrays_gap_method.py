# Time complexity: O(n log(n)) + O(n) = O(n log n).
# n log(n) for sorting the second array.
# O(n) for traversing the array.  

def mergeArraysGapMethod(a1, a2):
    n1 = len(a1)
    n2 = len(a2)

    n = n1 + n2
    gap = n // 2

    while gap > 0:
        i = 0
        j = i + gap

        # dealing with the first array
        while j < n1:
            if a1[i] > a1[j]:
                a1[i], a1[j] = a1[j], a1[i]
            j += 1
            i += 1

        # Important Step
        if gap > n1:
            j = gap - n1
        else:
            j = 0

        # dealing with the second array
        while j < n2 and i < n1:
            if a1[i] > a2[j]:
                a1[i], a2[j] = a2[j], a1[i]
            i += 1
            j += 1

        # if there are more places to visit in second array
        if j < n2:
            j = 0
            while j + gap < n2:
                if (a2[j] > a2[j + gap]):
                    a2[j], a2[j + gap] = a2[j + gap], a2[j]
                j += 1

        # decrementing the gap
        gap = gap // 2


if __name__ == '__main__':
    a1 = [1, 4, 7, 8, 10]
    a2 = [2, 3, 9]

    mergeArraysGapMethod(a1, a2)
    print(a1)
    print(a2)
