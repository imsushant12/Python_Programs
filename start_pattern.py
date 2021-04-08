n = int(input("Enter number of rows : "))

type = int(input("Enter 1 to print straight or 0 to print reverse : "))
bool(type)

if type == True:
    for row in range(n):
        for column in range(row+1):
            print("*" , end=" ")
        print()

elif type == False:
    for row in range(n,0,-1):   #n to 0 (reverse order) i.e n--
        for column in range(row):
            print("*" , end=" ")
        print()
