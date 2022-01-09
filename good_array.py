'''
Problem Statement:
------------------
You are given Q queries such that each query contains two integers (N[i], D[i]). 
The answer for each query is equal to the sum of score of all possible good arrays
with length N[i].
An array is good array if there are N elements in the array and all the elements in
the array lie between 1 and N (both included).
'''

def sum(a):
    sum = 0
    for i in range(0, len(a)):    
        sum += a[i]; 
    return sum

def solve(queries):
    counter = 0
    while queries:
        queries -= 1
    
        n = int(input())
        d = int(input())

        arrays = []
        for i in range(1, n+1):
            for j in range(1,i+2):
                if i < n and j < n:
                    arrays.append([i, j])

        for i in range(len(arrays)):
            if sum(arrays[i]) == d:
                counter += 1

        print(counter)

if __name__ == "__main__":
    queries = int(input())
    solve(queries)
 