import sys
sys.stdin = open('input.txt')

dice_back = {0 : 5, 1 : 3, 2 : 4, 3 : 1, 4 : 2, 5 : 0}

n = int(input())
dice = [list(map(int,input().split())) for _ in range(n)]
print(dice)
rlt = 0
for i in range(6):
    tmp = 0
    for j in range(n):
        down = dice[j][i]
        up = dice[j][dice_back[i]]
        dice.remove(down)
        dice.remove(up)

        print(down, up)
