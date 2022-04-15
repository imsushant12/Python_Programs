"""
Problem Statement:
------------------
Given a matrix mat[][], print it in Wave Form. 

Input: mat[][] = {
                    {  1, 2,  3,  4 }
                    {  5, 6,  7,  8 }
                    {  9, 10, 11, 12}
                    { 13, 14, 15, 16}
                    { 17, 18, 19, 20}
                 }
Output: 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19 20 16 12 8 4 

Input: mat[][] = {
                    { 1,  9,  4, 10}
                    { 3,  6, 90, 11}
                    { 2, 30, 85, 72}
                    { 6, 31, 99, 15}
                } 
Output: 1 3 2 6 31 30 6 9 4 90 85 99 15 72 11 10
"""


def solve(array, row, col):
    flag = True         # true resembles up to down printing
    for j in range(col):
        if flag:
            for i in range(row):
                print(array[i][j], end = " ")
            flag = False
        else:
            for i in range(row-1, -1, -1):
                print(array[i][j], end= " ")
            flag = True


if __name__ == "__main__":
    array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    row = 3
    col = 3
    solve(array, row, col)
