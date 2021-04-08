n = int(input("Enter size of list : "))
print("Enter the numbers ")
i=0
sum=0
num = []
for i in range(n):
    num.insert(i , int(input()))
    sum = sum + int(num[i])
print("Sum = " , sum)