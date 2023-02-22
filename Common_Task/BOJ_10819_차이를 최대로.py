import sys
sys.stdin = open('input.txt')

import itertools

def abs_sub(a, b):
    if (a - b) < 0:
        rlt = (a - b)*(-1)
    else:
        rlt = a - b
    return rlt

n = int(input())
A = list(map(int, input().split()))
rlt = 0
for i in list(itertools.permutations(A)):
    tmp = 0
    for j in range(n-1):
        tmp += abs_sub(i[j], i[j+1])
    if rlt <= tmp:
        rlt = tmp

print(rlt)