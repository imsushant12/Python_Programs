def fibs(n):                                                                                                 
    fibs = [0, 1, 1]                                                                                           
    for f in range(2, n):                                                                                      
        fibs.append(fibs[-1] + fibs[-2])                                                                         
    return fibs[n]

def result(fibs, m):
    sum = 0
    for i in fibs:
        if i % m == 0:
            sum += i
    
    print(sum)
n = int(input())
m = int(input())
fibs = fibs(n)
result(fibs, m)