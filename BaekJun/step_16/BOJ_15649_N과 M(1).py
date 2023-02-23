import sys
sys.stdin = open('input.txt')

def perm(arr):
    if len(arr) == m:
        print(*arr)

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            arr.append(num[i])
            perm(arr)
            visited[i] = 0
            arr.pop()

n, m = map(int, input().split())
num = list(range(1, n+1))
visited = [0] * n

perm([])

