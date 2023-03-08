import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
basket = [0] * n
for _ in range(m):
    i, j, k = map(int, input().split())
    for l in range(i-1, j):
        basket[l] = 0
        basket[l] = k
print(*basket)