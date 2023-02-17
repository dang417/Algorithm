import sys
sys.stdin = open('sample_input.txt')

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    # 모든 L에 대해서
    # W가 있는 곳
    arr = [list(input()) for _ in range(n)]
    point_d = {}
    w_cnt = 0
    w_idx = []
    for i in range(n):
        w_cnt += arr[i].count('W')
    print(arr)
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'W':
                point_d[(i, j)] = 0
                w_idx.append((i, j))
            else:
                point_d[(i, j)] = 1000
    print(point_d)

    for i in range(n):
        for j in range(m):
            for w in w_idx:
                if abs(w[0] - i) + abs(w[1] - j) <= point_d[(i, j)]:
                    point_d[(i, j)] = abs(w[0] - i) + abs(w[1] - j)

    print(f'#{tc}', sum(point_d.values()))
    # 각 w에 대해서 모든 땅에서 가는 거리를 찾아서
    # 그 중에 가장 작은 값을 딕셔너리 i, j의 value 로 지정