import sys
sys.stdin = open('input.txt')

n = int(input())
arr = [[0] * 1001 for _ in range(1001)]
paper_dict = {i : 0 for i in range(1, n + 1)}
rlt = 0

for i in range(1, n + 1):
    x, y, w, h = map(int, input().split())
    for j in range(h):
        for k in range(w):
            arr[y + j][x + k] = i

for i in arr:
    if sum(i) == 0:
        continue
    for j in range(1, n+1):
        paper_dict[j] += i.count(j)

for i in range(1, n+1):
    print(paper_dict[i])