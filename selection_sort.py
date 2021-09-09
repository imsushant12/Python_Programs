def selectionSort(a):
    n = len(a)

    for i in range(n):
        k = i
        for j in range(i+1 , n):
            if(a[j] < a[k]):
                k = j
        a[i], a[k] = a[k], a[i]


a = [64, 34, 25, 82, 22, 11, 90]
selectionSort(a)

print("Sorted array : ")
for i in a:
    print(i)
