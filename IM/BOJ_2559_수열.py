import sys
sys.stdin = open('input.txt')

n = int(input())
seq = list(map(int, input().split()))
max_cnt = 1
cnt = 1
for i in range(1, n):
    if seq[i - 1] >= seq[i]:
        cnt += 1
    else:
        if max_cnt <= cnt:
            max_cnt = cnt
        cnt = 1

if max_cnt <= cnt:
    max_cnt = cnt

cnt = 1
for i in range(1, n):
    if seq[i - 1] <= seq[i]:
        cnt += 1
    else:
        if max_cnt <= cnt:
            max_cnt = cnt
        cnt = 1

if max_cnt <= cnt:
    max_cnt = cnt

print(max_cnt)