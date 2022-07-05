def merge(a, s, mid, e):
    answer = 0
    
    left = a[:mid]
    right = a[mid:]

    i = 0       # for left array
    j = 0       # for right array
    k = 0       # for main array

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
            k += 1
        # left[i] > right[j] then all the left array elements
        # will be larger than right[j].
        else:
            a[k] = right[j]
            answer += (len(left) - i + 1)
            k += 1
            j += 1

        while i < len(left):
            a[k] = left[i]
            k += 1
            i += 1

        while j < len(right):
            a[k] = right[j]
            k += 1
            j += 1

    return answer

def mergeSort(a, s, e):
    answer = 0
    if s < e:
        mid = (s + e) // 2
        answer += mergeSort(a, s, mid)
        answer += mergeSort(a, mid+1, e)
        answer += merge(a, s, mid, e)
            
    return answer
        
def inversionCount(a, n):
    """
    # Simple Approach:
    # -----------------
    counter = 0
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                counter += 1
                
    return counter
    """
    
    # Using the logic of mergeSort, we can divide the array and count the inversions
    answer = mergeSort(a,0,n)
    return answer

a = [ 3, 2, 1 ]
print(inversionCount(a, len(a)))