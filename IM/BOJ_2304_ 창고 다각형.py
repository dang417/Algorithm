import sys
sys.stdin = open('input.txt')

n = int(input())
storage = [0] * 1001
for i in range(n):
    l, h = map(int, input().split())
    storage[l] = h
max_idx = storage.index(max(storage))
height = 0
rlt = 0

for i in range(max_idx + 1):
    if height <= storage[i]:
        height = storage[i]
    rlt += height

height = 0
for i in range(1001 - 1, max_idx, -1):
    if height <= storage[i]:
        height = storage[i]
    rlt += height
print(rlt)