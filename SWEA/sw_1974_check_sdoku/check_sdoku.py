import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    matrix = []
    for i in range(9):
        row = list(map(int,input().split()))
        matrix.append(row)
        for j in range(8):
            if row[j] in row[j+1:]:
                rlt = 0
                break
    for i in range(8):
        for j in range(9):
            if matrix[i][j] in matrix[i+1:][j]:
                rlt = 0
                break
    else: rlt = 1

    for i in (0, 3, 6):
        

    if rlt == 1:
        print(1)
    else :
        print(0)