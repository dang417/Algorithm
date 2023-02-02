import sys
sys.stdin = open('s_input.txt')

t = int(input())

for tc in range(1, t+1):
    D, A, B, F = map(int,input().split())
    rlt = (D / (A + B)) * F
    print(f'#{tc} {rlt}')