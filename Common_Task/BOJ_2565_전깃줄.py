import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n = int(input())
line = sorted([list(map(int, input().split())) for _ in range(n)])

dp = [1] * n
for i in range(n):
    for j in range(i):
        if line[i][1] > line[j][1]:
            # 만약 i,1 이 j,1 보다 크다면
            # j의 증가하는 가장 긴 부분수열의 길이 + 1 과 현재 i의 길이를 비교해
            # 더 긴쪽을 택함
            dp[i] = max(dp[i], dp[j] + 1)

print(len(line) - max(dp))