import sys
sys.stdin = open('input.txt')

def perm(arr, a = 1):
    if len(arr) == m:
        rlt.append(arr)
        print(*arr)
        return

    for i in range(a-1, n):
        if visited[i] <= m:
            visited[i] += 1
            arr.append(num[i])
            perm(arr, num[i])
            visited[i] -= 1
            arr.pop()

n, m = map(int, input().split())
num = list(range(1, n+1))
rlt = []
visited = [0] * n
perm([])
