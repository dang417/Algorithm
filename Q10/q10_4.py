import sys
input = sys.stdin.readline

t = int(input())
num = []
for i in range(t):
    num.append(int(input()))
for i in sorted(num):
    print(i)