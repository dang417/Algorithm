import sys
sys.stdin = open('sample_input.txt')

from collections import deque

def BFS():
    visited = [[0] * m for _ in range(n)]
    q = deque([])


t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(n)]
