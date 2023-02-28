import sys
sys.stdin = open('s_input.txt')

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    row = [[arr[i][0], arr[i][1], arr[i][2], arr[i][3], arr[i][4]] for i in range(n)]
    col = [[arr[0][i], arr[1][i], arr[2][i], arr[3][i], arr[4][i]] for i in range(n)]
    cross = [[arr[0][0], arr[1][1], arr[2][2], arr[3][3], arr[4][4]],
             [arr[0][4], arr[1][3], arr[2][2], arr[3][1], arr[4][0]]]

    for i in range(n):
        if row[i] == ['o', 'o', 'o', 'o', 'o'] or col[i] == ['o', 'o', 'o', 'o', 'o'] or cross[0] == ['o', 'o', 'o', 'o', 'o'] or cross[1] == ['o', 'o', 'o', 'o', 'o']:
            rlt = 'YES'
            break
        else:
            rlt = 'NO'

    print(f'#{tc}', rlt)
