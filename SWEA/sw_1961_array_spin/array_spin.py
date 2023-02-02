import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    matrix = []
    degree_90 = []
    degree_180 = []
    degree_270 = []
    
    for num in range(n):
        row = list(map(int,input().split()))
        matrix.append(row)
        for i in range(len(matrix)):
            tmp = []
            for j in range(len(matrix)):
                tmp.append(matrix[-(j+1)][i])
            if len(tmp) == n:
                degree_90.append(tmp)
        
        for i in range(len(matrix)):
            tmp = []
            for j in range(len(matrix)):
                tmp.append(matrix[-(i+1)][-(j+1)])
            if len(tmp) == n:
                degree_180.append(tmp)

        for i in range(len(matrix)):
            tmp = []
            for j in range(len(matrix)):
                tmp.append(matrix[j][-(i+1)])
            if len(tmp) == n:
                degree_270.append(tmp)
    print(f'#{tc}')
    for i in range(n):
        for j in range(n):
            print(degree_90[i][j], end = '')
        print(' ', end = '')
        for j in range(n):    
            print(degree_180[i][j], end = '')
        print(' ', end = '')
        for j in range(n):
            print(degree_270[i][j], end = '')
        print()