# NXM 배열에 데이터들 저장하고 난 후
# 가장 긴 구조물의 길이를 구해야 하고
# 각 구조물은 1이란 데이터로 주어지므로
# 행과 열을 순회하며 데이터가 0이 아닐때마다 계속해서 += 1
# 0을 만나면 최대값인지 비교 후 저장 AND 초기화
# 최대값 출력
import sys
sys.stdin = open('input1.txt')

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr_row = [0] * n
    arr_col = []
    max_len = []

    for i in range(n):
        row = ''.join(input().split())
        arr_row[i] = row

    for i in range(m):
        col = ''
        for j in range(n):
            col += arr_row[j][i]
        arr_col.append(col)

    # 가로 조사
    for rows in arr_row:
        i = 0
        cnt = 0
        while i < m:
            if rows[i] == '1':
                i += 1
                cnt += 1

            else:
                i += 1
                max_len.append(cnt)
                cnt = 0

        max_len.append(cnt)
        cnt = 0
    # 세로 조사
    for cols in arr_col:
        i = 0
        cnt = 0
        while i < n:
            if cols[i] == '1':
                i += 1
                cnt += 1

            else:
                i += 1
                max_len.append(cnt)
                cnt = 0

        max_len.append(cnt)
        cnt = 0
    a = max(max_len)
    if a <= 2:
        a = 0

    print(f'#{tc}', a)