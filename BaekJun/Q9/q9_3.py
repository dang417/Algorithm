t = int(input())
matrix = [[0]*101 for i in range(101)]
tmp = []
rlt = 0
for case in range(t):
    x,y = map(int,input().split())
    for row in range(x,x+10):
        for col in range(y,y+10):
            matrix[row][col] = 1

for k in range(len(matrix)):
    rlt += sum(matrix[k])

print(rlt)