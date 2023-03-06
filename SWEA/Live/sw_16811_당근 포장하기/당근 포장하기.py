import sys
sys.stdin = open('sample_in.txt')

# 소 중 대 상자로 구분
# 같은 크기의 당근은 같은 상자
# 비어있는 상자 X
# 한 상자에 N/2를 초과하는(과반 이상)의 당근 X
#
# t = int(input())
# for tc in range(1, t+1):
#     N = int(input())
#     carrot = sorted(list(map(int, input().split())))
#     rlt = N
#     for i in range(N-2):
#         for j in range(i+1, N-1):
#             s = carrot[:i+1]
#             m = carrot[i+1:j+1]
#             l = carrot[j+1:]
#             if len(s) > N//2 or len(m) > N//2 or len(l) > N//2:
#                 continue
#             elif set(s) & set(m) or set(s) & set(l) or set(m) & set(l):
#                 continue
#             elif rlt >= max(abs(len(s)-len(m)), abs(len(s)-len(l)), abs(len(m)-len(l))):
#                 rlt = max(abs(len(s)-len(m)), abs(len(s)-len(l)), abs(len(m)-len(l)))
#
#     if rlt >= N//2:
#         rlt = -1
#     print(f'#{tc}', rlt)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrot = list(map(int, input().split()))
    carrot.sort()

    minV = 1000
    for i in range(N-2):  # 소 박스
        for j in range(i+1, N-1):  # 중 박스
            # 같은 크기가 다른 박스에 들어가는 경우 제외하고
            if carrot[i] != carrot[i+1] and carrot[j] != carrot[j+1]:
                A = i + 1
                B = j - i
                C = N - 1 - j
                if A * B * C != 0 and A <= N//2 and B <= N//2 and C <= N//2:
                    if minV > max(A, B, C) - min(A, B, C):
                        minV = max(A, B, C) - min(A, B, C)
    if minV == 1000:
        minV = -1

    print(f'#{tc} {minV}')