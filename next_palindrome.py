"""
Problem Statement:
-----------------
A palindrome is a string that, when reversed, is equal to itself. Example of the palindrome includes:
676, 616, mom, 100001.

You have to take a number as an input from the user. You have to find the next palindrome corresponding to that number.
Your first input should be the number of test cases and then take all the cases as input from the user.

Input:
3
451
10
2133

Output:
Next palindrome for 451 is 454
Next palindrome for 10 is 11
Next palindrome for 2211 is 2222
"""

def checkPalindrome(s):
    return s == s[ : : -1]
    # #Other way:
    # l = len(s)
    # for i in range((l//2) + 1):
    #     if s[i] != s[l-1-i]:
    #         return False
    #     return True



t = int(input("Enter number of test cases : "))

while t:
    t -= 1
    s = input("Enter the number : ")
    if checkPalindrome(s):
        print("Entered number is itself a palindrome.")
    else:
        num = int(s)
        while True:
            num = num + 1
            if checkPalindrome(str(num)):
                print(f"Next palindrome number after {s} is : " + str(num))
                break