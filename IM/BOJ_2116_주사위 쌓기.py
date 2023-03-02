import sys
sys.stdin = open('input.txt')

dice_back = {0 : 5, 1 : 3, 2 : 4, 3 : 1, 4 : 2, 5 : 0}

n = int(input())
dice = [list(map(int,input().split())) for _ in range(n)]
rlt = 0
for i in range(6):
    tmp = 0
    down = dice[0][i]
    up = dice[0][dice_back[i]]
    if 6 in [down, up]:
        if 5 in [down, up]:
            tmp += 4
        else:
            tmp += 5
    else:
        tmp += 6
    for j in range(1, n):
        down = up
        up = dice[j][dice_back[dice[j].index(down)]]
        if 6 in [down, up]:
            if 5 in [down, up]:
                tmp += 4
            else: tmp += 5
        else:
            tmp += 6
    if rlt <= tmp:
        rlt = tmp

print(rlt)
