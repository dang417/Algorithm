t = int(input())
for tc in range(1, t+1):
    n = int(input())
    numbers = input()

    counts = [0] * 10

    for num in numbers:
        counts[int(num)] += 1
    max_cnt = 0
    idx = 0
    for i in range(len(counts)-1, 0, -1):
        if counts[i] > max_cnt:
            max_cnt = counts[i]
            idx = i

    print(f'#{tc} {idx} {max_cnt}')