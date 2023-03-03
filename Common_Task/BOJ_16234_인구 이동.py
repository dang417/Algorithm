import sys
sys.stdin = open('input.txt')
from collections import deque

N, L, R = map(int, input().split())
world = [list(map(int, input().split())) for _ in range(N)]
open_border()