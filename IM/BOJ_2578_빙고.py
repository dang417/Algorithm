import sys
sys.stdin = open('input.txt')

board = [list(map(int, input().split())) for _ in range(5)]
row = [[] * 5 for _ in range(5)]
col = [[] * 5 for _ in range(5)]
cross = [[] * 5 for _ in range(2)]

for i in range(5):
    cross[0] += [board[i][i]]
    cross[1] += [board[i][4-i]]
    for j in range(5):
        row[i] += [board[i][j]]
        col[i] += [board[j][i]]

numbers = [list(map(int, input().split())) for _ in range(5)]
cnt = 0
for i in range(5):
    for j in range(5):
        for k in range(5):
            if numbers[i][j] in row[k]:
                row[k].remove(numbers[i][j])
                if row[k] == []:
                    cnt += 1
            if numbers[i][j] in col[k]:
                col[k].remove(numbers[i][j])
                if col[k] == []:
                    cnt += 1
        for k in range(2):
            if numbers[i][j] in cross[k]:
                cross[k].remove(numbers[i][j])
                if cross[k] == []:
                    cnt += 1
        if cnt >= 3:
            print((i*5)+(j+1))
            exit()