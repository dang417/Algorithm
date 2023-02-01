import sys

matrix = []

# 비어있는 매트릭스 생성

for i in range(9):
    num = list(map(int,sys.stdin.readline().split()))
    matrix.append(num)

# 입력값을 리스트로 빈 매트릭스에 저장

max_num = 0
row = 0

for i in range(9):
    if max_num < max(matrix[i]):
        max_num = max(matrix[i])
        row = i

# max_num에 각 행을 순회하며 비교해서 최댓값을 저장
# 그때 그 행의 값을 row 에 저장

print(max_num)
print(row+1, matrix[row].index(max_num)+1)

# 그 최댓값과 해당하는 행 
# 그리고 그 행에서 최댓값의 위치를 index 해서 출력