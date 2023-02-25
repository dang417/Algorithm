import sys
sys.stdin = open('sample_input.txt')

from collections import deque

t = int(input())
for tc in range(1, t+1): # 각 터널 타입에 따라 이동할 수 있는 방향이 저장된 델타 값
    tunnel_delta = {1 : [[-1, 1, 0, 0], [0, 0, -1, 1]],
                   2 : [[-1, 1, 0, 0], [0, 0, 0, 0]],
                   3 : [[0, 0, 0, 0], [0, 0, -1, 1]],
                   4 : [[-1, 0, 0, 0], [0, 0, 0, 1]],
                   5 : [[0, 1, 0, 0], [0, 0, 0, 1]],
                   6 : [[0, 1, 0, 0], [0, 0, -1, 0]],
                   7 : [[-1, 0, 0, 0], [0, 0, -1, 0]]
                   }
    # 각 델타에 따라서 i, j 에서 갈 수 있는 터널 타입의 종류들이 정리된 딕셔너리
    tunnel_type = {1: [[1, 2, 5, 6], [1, 2, 4, 7], [1, 3, 4, 5], [1, 3, 6, 7]],
                    2: [[1, 2, 5, 6], [1, 2, 4, 7], [0], [0]],
                    3: [[0], [0], [1, 3, 4, 5], [1, 3, 6, 7]],
                    4: [[1, 2, 5, 6], [0], [0], [1, 3, 6, 7]],
                    5: [[0], [1, 2, 4, 7], [0], [1, 3, 6, 7]],
                    6: [[0], [1, 2, 4, 7], [1, 3, 4, 5], [0]],
                    7: [[1, 2, 5, 6], [0], [1, 3, 4, 5], [0]]
                    }

    n, m, r, c, l = map(int, input().split())
    tunnel_map = [list(map(int, input().split())) for _ in range(n)]
    fugitive = [[0] * m for _ in range(n)]
    fugitive[r][c] = 1
    q = deque((r, c))
    rlt = 0
    # BFS
    while q:
        i = q.popleft()
        j = q.popleft()
        # 저장된 딕셔너리에서 델타 값 불러오기
        if tunnel_map[i][j]:
            di = tunnel_delta[tunnel_map[i][j]][0]
            dj = tunnel_delta[tunnel_map[i][j]][1]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < m:
                    # 델타에 따른 다음 자리에 터널이 있는지와 visited 검사
                    if tunnel_map[ni][nj] and not fugitive[ni][nj]:
                        # 다음 자리의 터널 타입이 현재 델타 진행 방향에서 갈 수 있는 곳인지 검사
                        if tunnel_map[ni][nj] in tunnel_type[tunnel_map[i][j]][k]:
                            q.append(ni)
                            q.append(nj)
                            # 시간의 경과를 저장하기 위해 이전 인덱스에서 +1
                            fugitive[ni][nj] = fugitive[i][j] + 1
    # 가능한 모든 터널을 출력하기 위해 주어진 시간 이하의 모든 시간에 해당하는 개수 세기
    for i in range(n):
        for j in range(m):
            if 0 < fugitive[i][j] <= l:
                rlt += 1
    print(f'#{tc}', rlt)