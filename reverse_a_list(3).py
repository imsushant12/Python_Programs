def reverseList(list):
    l = len(list)
    for i in range(l//2):
        list[i] , list[l-1-i] = list[l-1-i] , list[i]

list = [10 , 25 , 11 , 5 , 69 , 45]

reverseList(list)
print(list)
