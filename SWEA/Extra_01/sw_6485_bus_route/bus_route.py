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

'''
교수님 풀이
for test_case in range(1, t+1)
    N = int(input())
    # [1] N번 반복하면서 노선 입력, 빈도수 표시
    cnts = [0] * 5001
    for _ in range(N):
        S, E = map(int,input().split())
        for i in range(S, E+1):
            cnts[i] += 1
    
    P = int(inpput())
    alst = []
    for _ in range(P):
        p = int(input())
        alst.append(cnts[p])
        
    print(f'#{test_case}', *alst)
'''






