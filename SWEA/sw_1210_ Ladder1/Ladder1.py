# 사다리의 배열을 표현하고 나서
# 1행에 존재하는 모든 출발점(data[i][j])에 대해서
# 0. 출발점의 인덱스를 x 에 저장
# 1. 좌우 데이터 검사
#    만약 좌 또는 우에 1 데이터 존재하면 j -= 1 or j += 1
#    없다면 i += 1
# 2. data[i][j] == 2 일 때까지 (도착점의 데이터가 2)
import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    t = int(input())
    matrix = []
    for i in range(100):
        row = list(map(int, input().split()))
        matrix.append(row)
    for i in range(100):
        a = 0
        b = i
        if matrix[a][b] == 1: # 시작점 확인
            # 내려가다가 왼쪽 또는 오른쪽으로 가는 길을 만나면 움직임
            while a < 99:
                # 범위를 벗어나면 안되기 때문에 범위 안에 있는지 부터 확인하고 길 탐색
                if b >= 1 and matrix[a][b-1] == 1:
                    # 길이 있으면 길이 없을때까지 계속 진행
                    while b > 0 and matrix[a][b-1] == 1:
                        b -= 1
                    a += 1
                # 범위를 벗어나면 안되기 때문에 범위 안에 있는지 부터 확인하고 길 탐색
                elif b <= 98 and matrix[a][b+1] == 1:
                    # 길이 있으면 길이 없을때까지 계속 진행
                    while b < 99 and matrix[a][b+1] == 1:
                        b += 1
                    a += 1
                # 좌 우에 길이 없는 경우 내려감
                else:
                    a += 1

        if matrix[a][b] == 2:
            print(f'#{tc}',i)










