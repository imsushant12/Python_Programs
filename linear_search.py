def naive_search(l , target):
    for i in l:
        if (i == target):
            return 1
        return -1    # Else condition.

l = [10 , 20 , 1 , 25 , 45 , 85 , 78 , 69 , 100]
target = 45

if (naive_search(l , target)):
    print("Target found!")
else:
    print("Target not found!")