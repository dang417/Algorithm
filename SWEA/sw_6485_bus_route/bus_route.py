import sys
sys.stdin = open('s_input.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    A = []
    B = []
    C = []
    for i in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    p = int(input())
    rlt = [0] * p

    for j in range(p):
        C.append(int(input()))

    for k in range(len(C)):
        for l in range(n):
            if A[l] <= C[k] <= B[l]:
                rlt[k] += 1

    print(f'#{tc}', *rlt)

