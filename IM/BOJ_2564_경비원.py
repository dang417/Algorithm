import sys
sys.stdin = open('input.txt')

m, n = map(int, input().split())

direction = {1 : 0, 2 : n - 1, 3 : 0, 4 : m - 1}
points = {}

for i in range(1, int(input())+1):
    d, l = map(int, input().split())
    if d == 1:
        points[i] = [0, l]
    elif d == 2:
        points[i] = [n, l]
    elif d == 3:
        points[i] = [l, 0]
    elif d == 4:
        points[i] = [l, m]

dk_d, dk_l = map(int, input().split())
if dk_d == 1:
    points['d'] = [0, dk_l]
elif dk_d == 2:
    points['d'] = [n, dk_l]
elif dk_d == 3:
    points['d'] = [dk_l, 0]
elif dk_d == 4:
    points['d'] = [dk_l, m]

print(points)


points['d'][0]