t = int(input())

for tc in range(1, t+1):
    n = int(input())
    clothes = {}
    clothes_cnt = {}
    for i in range(n):
        x, y = input().split()
        clothes[y] = x
        clothes_cnt = 0
    