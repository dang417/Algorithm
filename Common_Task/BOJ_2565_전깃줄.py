import sys
sys.stdin = open('input.txt')

n = int(input())
line = [[0, 0] for _ in range(n+1)]
rlt_cnt = 0

for i in range(1, n+1):
    line[i][0], line[i][1] = map(int, input().split())

while True:
    line_dict = {i : 0 for i in range(501)}
    for i in range(1, n+1):
        for j in range(1, n+1):
            if line[i][0] < line[j][0] and line[i][1] > line[j][1]:
                line_dict[line[i][0]] += 1
            elif line[i][0] > line[j][0] and line[i][1] < line[j][1]:
                line_dict[line[i][0]] += 1

    for i in range(1, n+1):
        if line_dict[line[i][0]] == max(line_dict.values()):
            line[i] = [0, 0]
            break

    if sum(line_dict.values()) == 0:
        break
    rlt_cnt += 1

print(rlt_cnt)