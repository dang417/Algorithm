import sys
sys.stdin = open('input.txt')

m, n = map(int, input().split())
arr = [[0] * (m + 1) for _ in range(n + 1)]

x = int(input())
store = [[0, 0] for _ in range(x)]

for o in range(x):
    store[o][0], store[o][1] = map(int, input().split())

i, j = map(int, input().split())






