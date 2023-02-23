import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    heap = [0] + list(map(int, input().split()))
    rlt = 0

    for i in range(1, n + 1):
        while heap[i // 2] > heap[i]:
            heap[i // 2], heap[i] = heap[i], heap[i // 2]
            i = i // 2

    n = n // 2
    while n > 0:
        rlt += heap[n]
        n = n // 2

    print(f'#{tc}', rlt)