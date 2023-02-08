n, m = map(int,input().split())

card_list = list(map(int,input().split()))

card_sum = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            tmp = card_list[i] + card_list[j] + card_list[k]
            if card_sum <= tmp <= m:
                card_sum = tmp

print(card_sum)


