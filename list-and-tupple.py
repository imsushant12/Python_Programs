n = int(input("Enter size of list : "))
print("Enter the numbers ")
i=0
sum=0
fruits = []
for i in range(n):
    fruits.insert(i,input())
    sum = sum + int(fruits[i])
print(fruits)
print(sum)