import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    rows = []
    cols = []
    blocks = []
    rlt = 1
    # 스도쿠 행들만 모아서 리스트
    for i in range(9):
        row = list(map(int, input().split()))
        rows.append(row)
    # 스도쿠 열들만 모아서 리스트
    for i in range(9):
        col = []
        for j in range(9):
            col.append(rows[j][i])
        cols.append(col)
    # 행과 열 안에서 중복 검사
    for i in range(9):
        for j in range(8):
            if rows[i][j] in rows[i][j+1:]:
                rlt = 0
            if cols[i][j] in cols[i][j+1:]:
                rlt = 0
    # 스토쿠 블럭만 모아서 리스트
    for l in (0, 3, 6):
        for i in (0, 3, 6):
            block = []
            for j in range(3):
                for k in range(3):
                    block.append(rows[j+l][i + k])
            blocks.append(block)
    # 블럭 안에서 중복 검사
    for i in range(9):
        for j in range(8):
            if blocks[i][j] in blocks[i][j+1:]:
                rlt = 0
    # 모두 아닐 경우 rlt = 1 유지
    print(f'#{tc} {rlt}')




