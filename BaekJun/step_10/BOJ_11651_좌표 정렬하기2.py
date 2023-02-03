import sys
input = sys.stdin.readline

# 좌표들을 입력받아 y 값을 key로 먼저 정렬한 뒤
# x 값을 좌표로 정렬

n = int(input())
point_list = []

for i in range(n):
    x, y = map(int,input().split())
    point_list.append([x,y])

point_list.sort(key = lambda x : (x[1], x[0]))

# lambda 함수를 활용해 각 점의 x 값과 y 값의 인덱스 위치를 바꾸어서
# 그것을 key로 리스트를 정렬

for j in point_list:
    print(j[0], j[1])