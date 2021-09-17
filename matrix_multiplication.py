A = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]

result = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

def findProduct():
    n = len(A)
    m = len(B[0])
    for i in range(n):
        for j in range(m):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    
    print("Product of the matrices are : ")        
    for r in result:
        print(r)

findProduct()

