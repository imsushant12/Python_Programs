def subtractProductAndSum(n):
        sum = 0
        product = 1
        
        while n > 0:
            remainder = (n % 10)
            print(remainder)
            sum += remainder
            product *= remainder
            
            n = n // 10
            
        return (product - sum)


print(subtractProductAndSum(234))