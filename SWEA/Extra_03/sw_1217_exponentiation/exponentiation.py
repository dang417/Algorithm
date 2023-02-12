# 재귀 호출을 이용하여
import sys
sys.stdin = open('input.txt')

def exponentiation(n, a):
    if a == 1:
        return n
    return n * exponentiation(n, a - 1)

for _ in range(1, 11):
    tc = int(input())
    n, a = map(int, input().split())
    print(f'#{tc}', exponentiation(n, a))