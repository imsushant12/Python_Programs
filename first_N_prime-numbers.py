def isPrime(n):
    count = 0
    for i in range(1 , n+1):
        if(n % i == 0):
            count += 1
    if count > 2:
        return False
    else:
        return True

def printPrimes(n):
    for i in range(2 , n+1):
        if(isPrime(i)):
            print(i)

n = int(input("Enter the value of n : "))

print(f"First {n} prime numbers are : ")
printPrimes(n)
