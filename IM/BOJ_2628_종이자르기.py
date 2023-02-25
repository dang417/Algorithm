import sys
sys.stdin = open('input.txt')

width, height = map(int, input().split())
n = int(input())
row_cut = []
col_cut = []
for i in range(n):
    d, num = map(int, input().split())
    if d == 0:
        row_cut.append(num)
    else:
        col_cut.append(num)

row_cut.sort()
col_cut.sort()

if row_cut:
    x = row_cut[0]
else:
    x = height
if col_cut:
    y = col_cut[0]
else:
    y = width

for i in range(len(row_cut)-1):
    if row_cut[i+1] - row_cut[i] >= x:
        x = row_cut[i+1] - row_cut[i]

for i in range(len(col_cut)-1):
    if col_cut[i+1] - col_cut[i] >= y:
        y = col_cut[i+1] - col_cut[i]

if row_cut:
    a = max(row_cut)
else:
    a = height

if col_cut:
    b = max(col_cut)
else:
    b = width

print(max(x, height - a) * max(y, width - b))