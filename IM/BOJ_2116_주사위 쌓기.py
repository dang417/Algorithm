import sys
sys.stdin = open('input.txt')

from collections import deque

n = int(input())

dice_tower = [list(map(int, input().split()))]
rlt = 0

for i in range(n-1):
    dice = deque(map(int, input().split()))
    while True:
        if dice_tower[i][0] == dice[-1]:
            break
        dice.rotate(1)
    dice_tower.append(list(dice))
print(dice_tower)
for i in dice_tower:
    print(i[1:5])


