import sys
sys.stdin = open('input.txt')

arr = [[0] * 100 for _ in range(100)]
rlt = 0

for i in range(4):
    ld_x , ld_y, ru_x, ru_y = map(int,input().split())
    for i in range(ld_y, ru_y):
        for j in range(ld_x, ru_x):
            arr[i][j] = 1

for rows in arr:
    rlt += sum(rows)

print(rlt)