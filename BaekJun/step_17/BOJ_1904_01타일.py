import sys
sys.stdin = open('input.txt')

n = int(input())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for i in range(3, 1000001):
    dp[i] = ((dp[i-1] % 15746) + (dp[i-2] % 15746)) % 15746

print(dp[n])