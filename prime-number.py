a = int(input("Enter a number : "))

flag = True

for i in range(2,a):
    if a%i == 0:
        flag = False

if flag is True:
    print("Prime")
else:
    print("Not prime")