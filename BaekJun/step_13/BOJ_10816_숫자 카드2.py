n = int(input())
sk_card = list(map(int,input().split()))
m = int(input())
card = list(map(int,input().split()))
cnt_dict = {}
rlt = [0] * m

for i in sk_card:
    cnt_dict[i] = 0

for i in sk_card:
    cnt_dict[i] += 1

for i in range(m):
    if card[i] in cnt_dict:
        rlt[i] = cnt_dict[card[i]]

print(*rlt)