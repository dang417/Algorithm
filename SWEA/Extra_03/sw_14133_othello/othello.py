import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [[0] * (n+2) for _ in range(n+2)]
    o = n//2
    arr[o][o] = arr[o+1][o+1] = 2
    arr[o+1][o] = arr[o][o+1] = 1

    for _ in range(m):
        si, sj, d = map(int, input().split())
        arr[si][sj] = d
        # 8방향 처리
        for di, dj in ((-1, -1,), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
            tlst = []
            for mul in range(1, n):
                ni, nj = si + (di * mul), sj + (dj * mul)
                if arr[ni][nj] == 0:
                    break
                elif arr[ni][nj] != d:  # 다른 돌인 경우 뒤집기 후보에 추가
                    tlst.append((ni, nj))
                else:                   # 같은 돌 -> 후보돌을 뒤집음
                    while tlst:
                        ti, tj = tlst.pop()
                        arr[ti][tj] = d
                    break
    bcnt = wcnt = 0
    for lst in arr:
        bcnt += lst.count(1)
        wcnt += lst.count(2)

    print(f'#{tc} {bcnt} {wcnt}')