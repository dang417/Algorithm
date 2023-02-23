import sys
sys.stdin = open('input.txt')

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

stack = [0] * n

for i in range(n):
    stack[i] = max(arr[-(i+1)])
