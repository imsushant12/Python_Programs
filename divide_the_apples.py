"""
Problem Statement:
-----------------
Harry Potter has got 'N' number of apples. Harry has some students among whom, he wants to
distribute the apples.
You need to print whether a number in range mn to mx is a divisor of N or not.

Input:
------
Take inout n, mn and mx from user.

Output:
-------
Print whether the numbers between mn and mx are divisor of n or not.
If mn = mx, show that this is not a valid range and show the result for that number.
"""

n = int(input("Enter the numbers of apples Harry got : "))
mn = int(input("Enter the minimum number of students : "))
mx = int(input("Enter the maximum number of students : "))

if mn == mx or mx < mn:
    print("This is not a valid range.")
    if n % mn == 0:
        print(f"{mn} is not a divisor of {n}.")
else:
    for i in range(mn , mx+1):
        if n % i == 0:
            print(f"{i} is a divisor of {n}.")
        else:
            print(f"{i} is not a divisor of {n}.")