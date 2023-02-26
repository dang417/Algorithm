import sys
sys.stdin = open('input.txt')

def merge(heights, locations, d = 0):
    global rlt
    if not heights:
        return
    if len(heights) == 1:
        rlt += [locations + heights]
        return
    left = []
    right = []
    for i in range(len(locations)):
        if heights[i] == max(heights):
            rlt.append([locations[i], heights[i]])
            if i == len(locations)-1 or i == 0:
                return
            if d == 0:
                left = locations[:i]
                left_heights = heights[:i]
                right = locations[i+1:]
                right_heights = heights[i+1:]
            if d == 1:
                left = locations[:i]
                left_heights = heights[:i]
            if d == 2:
                right = locations[i + 1:]
                right_heights = heights[i + 1:]
    if d == 0 or d == 1:
        merge(left_heights, left, 1)
    if d == 0 or d == 2:
        merge(right_heights, right, 0)

n = int(input())
towers = []
locations = []
heights = []
rlt = []
ans = 0

for i in range(n):
    l, h = map(int, input().split())
    towers.append([l, h])

towers.sort(key = lambda x : x[0])

for i in range(n):
    locations.append(towers[i][0])
    heights.append(towers[i][1])

merge(heights, locations)
rlt.sort()

for i in range(len(rlt) - 1):
    if rlt[i][1] < rlt[i+1][1]:
        ans += (rlt[i+1][0]-rlt[i][0]) * rlt[i][1]
    else:
        ans += (rlt[i+1][0]-rlt[i][0]) * rlt[i+1][1]

ans += (max(rlt, key = lambda x : x[1])[1])

print(ans)