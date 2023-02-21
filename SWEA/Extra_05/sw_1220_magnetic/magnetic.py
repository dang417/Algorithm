import sys
sys.stdin = open('input.txt')


for t in range(1):
    n = int(input())
    table = [list(input().split()) for _ in range(100)]
    cnt = 0
    for j in range(100):
        for i in range(100):