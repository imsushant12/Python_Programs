def mergeSortedArrays(a, leftArray, rightArray):
    if len(a) > 1:
        # merging both the sorted arrays:
        i = 0  # denoting index of the leftArray
        j = 0  # denoting index of the rightArray
        mainArrayIndex = 0  # denoting index of main array
        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] < rightArray[j]:
                a[mainArrayIndex] = leftArray[i]
                i += 1
            else:
                a[mainArrayIndex] = rightArray[j]
                j += 1
            mainArrayIndex += 1

        # adding the rest of the elements if present
        while i < len(leftArray):
            a[mainArrayIndex] = leftArray[i]
            i += 1
            mainArrayIndex += 1

        while j < len(rightArray):
            a[mainArrayIndex] = rightArray[j]
            j += 1
            mainArrayIndex += 1


def mergeSort(a):
    if len(a) > 1:
        mid = len(a) // 2

        leftArray = a[:mid]
        rightArray = a[mid:]

        mergeSort(leftArray)
        mergeSort(rightArray)
        mergeSortedArrays(a, leftArray, rightArray)

        """
        # If we want a single function:
        # -----------------------------
        leftArray = []
        rightArray = []

        # copying first half of the array into the leftArray
        mainArrayIndex = 0
        while mainArrayIndex < mid:
            leftArray.append(a[mainArrayIndex])
            mainArrayIndex += 1

        # copying second half of the array into the rightArray
        mainArrayIndex = mid
        while mainArrayIndex < len(a):
            rightArray.append(a[mainArrayIndex])
            mainArrayIndex += 1
        

        # merging both the sorted arrays:
        i = 0  # denoting index of the leftArray
        j = 0  # denoting index of the rightArray
        mainArrayIndex = 0  # denoting index of main array
        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] < rightArray[j]:
                a[mainArrayIndex] = leftArray[i]
                i += 1
            else:
                a[mainArrayIndex] = rightArray[j]
                j += 1
            mainArrayIndex += 1

        # adding the rest of the elements if present
        while i < len(leftArray):
            a[mainArrayIndex] = leftArray[i]
            i += 1
            mainArrayIndex += 1

        while j < len(rightArray):
            a[mainArrayIndex] = rightArray[j]
            j += 1
            mainArrayIndex += 1
        """


if __name__ == "__main__":
    a = [12, 11, 5, 6, 7]

    print("Original Array: ", a)
    mergeSort(a)
    print("Sorted   Array: ", a)
