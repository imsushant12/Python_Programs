operator = input("Enter the operator: ")
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

try:
    if operator == "+":
        print(num1+num2)
    elif operator == "-":
        print(num1-num2)
    elif operator == "*":
        print(num1*num2)
    elif operator == "/":
        print(num1/num2)
    elif operator == "**":
        print(num1**num2)
except:
    print("Try another operator")
