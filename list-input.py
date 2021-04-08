n = int(input("Enter size of list : "))
print("Enter the fruits")
i=0
fruits = []
for i in range(n):
    a = input()
    fruits.insert(i,a)
print(fruits)