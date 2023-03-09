import sys
sys.stdin = open('input.txt')

n = int(input())
numbers = list(map(int, input().split()))

dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[1][i] = numbers[i]
for i in range(n):
    for j in range(n):
        dp[i][j] = dp[i-1][j]

print(max(max(dp[i]) for i in range(n)))