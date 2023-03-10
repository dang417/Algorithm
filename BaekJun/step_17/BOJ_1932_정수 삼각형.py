import sys
sys.stdin = open('input.txt')

n = int(input())

num = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * i for i in range(1, n+1)]
dp[-1] = num[-1]
for i in range(n-1, 0, -1):
    for j in range(i):
        dp[i-1][j] = max(num[i-1][j] + dp[i][j], num[i-1][j] + dp[i][j+1])

print(dp[0][0])