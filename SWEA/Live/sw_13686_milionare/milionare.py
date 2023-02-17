import sys
sys.stdin = open('s_input.txt')

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    lst = list(map(int, input().split()))

    i = ans = 0
    while i < n:
        i_mx = i
        for j in range(i+1, n):
            if lst[i_mx] < lst[j]:
                i_mx = j

        for j in range(i, i_mx):
            ans += lst[i_mx] - lst[j]

        i = i_mx + 1

    print(f'#{tc}', ans)

# t = int(input())
#
# for tc in range(1, t+1):
#     n = int(input())
#     price = list(map(int, input().split()))
#     # 리스트가 증가하는 동안 계속해서 삼
#     # 감소하는 순간 판매
#     rlt = 0
#     tmp = 0
#     idx = 0
#     # 1. 뒤 원소가 크지만 그 뒤에 더 큰게 있다
#     # 2. 앞의 원소가 크다
#     # 3.
#     if price[0] <= price[1]:
#         tmp -= price[0]
#     for i in range(1, n-1):
#         if price[i-1] < price[i] and price[i] > price[i+1]:
#             tmp += price[i] * (i - idx)
#             rlt += tmp
#             tmp = 0
#             idx = i + 1
#         elif price[i] <= price[i+1]:
#             tmp -= price[i]
#     if price[n-2] < price[n-1]:
#         tmp += price[n-1] * (i + 1 - idx)
#         rlt += tmp
#
#     print(f'#{tc}', rlt)