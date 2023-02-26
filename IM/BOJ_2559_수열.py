
import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
seq = list(map(int, input().split()))
rlt = sum(seq[0:k])
tmp = sum(seq[0:k])

for i in range(0, n-k):
    tmp -= seq[i]
    tmp += seq[i+k]
    if rlt <= tmp:
        rlt = tmp

print(rlt)