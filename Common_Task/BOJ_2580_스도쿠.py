import sys
sys.stdin = open('input.txt')
from collections import deque
def check_sdoku(r, c):
    if sum(sdoku[r]) == 45 and sum(sdoku[i][c] for i in range(9)) == 45:
        return True
    else:
        return False

sdoku = [list(map(int, input().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if not sdoku[i][j]:
            blank.append((i, j))

print(blank)
q = deque()
for idx in blank:
    r, c = idx
    q.append((r, c))
    for i in range(1, 9):
        if i != sdoku[r][c]:
            sdoku[r][c] = i
            if check_sdoku(r, c):
                break
            else:
                r, c = q.popleft()
for i in range(9):
    print(*sdoku[i])