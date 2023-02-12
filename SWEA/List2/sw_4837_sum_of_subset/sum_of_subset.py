t = int(input())
num_set = list(range(1, 13))

for tc in range(1, t+1):
    rlt = 0
    n, k = map(int, input().split())
    for i in range(1 << 12):
        subset = []
        sum_of_subset = 0
        for j in range(12):
            if i & (1 << j):
                subset.append(num_set[j])
                sum_of_subset += num_set[j]
        if len(subset) == n and sum_of_subset == k:
            rlt += 1
    print(f'#{tc} {rlt}')