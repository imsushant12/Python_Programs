# def find_max(l):
#     max = 0
#     for i in range(len(l)):
#         if max < l[i]:
#             print(l[i])
#             max = l[i]
#     return max

def find_max(l):
    max = 0
    for i in l:
        if max < i:
            print(i)
            max = i
    return max

l = [10, 20, 30, 5, 25, 11]
print("Maximum number in the list is : " , str(find_max(l)))