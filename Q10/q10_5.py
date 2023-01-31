import sys
input = sys.stdin.readline

n = int(input())

num = [0] * 10001

for i in range(n):
    num[int(input())] += 1

for j in range(n):
    if num[j] != 0:
        for k in range(num[j]):
            print(j)