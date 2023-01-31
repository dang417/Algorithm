import sys
input = sys.stdin.readline

n = int(input())

point_list = []

for i in range(n):
    x, y = map(int,input().split())
    point_list.append((x,y))

point_list = sorted(point_list)

for i in range(len(point_list)):
    print(point_list[i][0],point_list[i][1])