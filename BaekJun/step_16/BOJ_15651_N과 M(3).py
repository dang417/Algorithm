import sys
sys.stdin = open('input.txt')

def perm(arr):
    if len(arr) == m:
        print(*arr)
        return

    for i in range(n):
        if visited[i] <= m:
            visited[i] += 1
            arr.append(num[i])
            perm(arr)
            visited[i] -= 1
            arr.pop()

n, m = map(int, input().split())
num = list(range(1, n+1))
visited = [0] * n
perm([])