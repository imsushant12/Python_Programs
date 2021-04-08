a = int(input("Enter number 1 "))
b = int(input("Enter number 2 "))
c = int(input("Enter number 3 "))
d = int(input("Enter number 4 "))

if a>b and a>c and a>d:
    print(a , "is greatest")
elif b>a and b>c and b>d:
    print(b , " is greatest")
elif c>a and c>b and c>d:
    print(c , " is greatest")
else:
    print(d, " is greatest")


# #Other way

# #Greater of the two:

# if a>b:
#     g1 = a
# else:
#     g1 = b

# #Greater of the two:

# if c>d:
#     g2 = c
# else:
#     g2 = d

# if g1>g2:
#     print(g1, " is greatest")
# else:
#     print(g2, " is greatest")


