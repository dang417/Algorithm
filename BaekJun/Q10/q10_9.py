import sys
input = sys.stdin.readline

n = int(input())
point_list = []

for i in range(n):
    x, y = map(int,input().split())
    point_list.append((x,y))

point_list = sorted(point_list)

for point in point_list:
    if point[0] == 0:
        point_list.append(point)
        point_list.remove(point)

for point in point_list:
    print(point[0],point[1])

