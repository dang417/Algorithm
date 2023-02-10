import sys
input = sys.stdin.readline

n = int(input())
sk_card = set(map(int, input().split()))
m = int(input())
card = list(map(int,input().split()))

# 탐색의 경우 list를 탐색하면 O(N)의 시간복잡도를 가지고, set나 dict를 탐색하면 O(1)의 시간복잡도를 가진다.

for i in range(m):
    if card[i] in sk_card:
        card[i] = 1
    else:
        card[i] = 0
print(*card)