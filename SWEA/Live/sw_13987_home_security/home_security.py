import sys
sys.stdin = open('sample_input.txt')

from collections import deque

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

def BFS():
    q = deque([])
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    pay = 0
    

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(n)]
    rlt = 0
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                for k in range(n):
                    BFS()

