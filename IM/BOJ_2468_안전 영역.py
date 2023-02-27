import sys
sys.stdin = open('input.txt')

n = int(input())
rlt = 100000
arr = [list(map(int, input().split())) for _ in range(n)]
for i in range(max(max(arr))):
    tmp = 0
    for i in range(n):
        for j in range(n):
            arr[i][j] -= 1
        tmp += arr[j].count(0)
    if rlt >= (n*n) - tmp:
        rlt = (n*n) - tmp

print(rlt)