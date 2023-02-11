
# 8x8로 list 슬라이싱해서 테스트 케이스 생성
# 칠하는 방법 두가지 모두 탐색 (bwbw or wbwb)
# 둘 중 작은 값을 저장
# 각 테스트 케이스 중 가장 작은 값 저장
# 푸린
n, m = map(int, input().split())
mtx = []

for i in range(n):
    row = list(input())
    mtx.append(row)

min_cnt = 64
for i in range(n-7):
    for j in range(m-7):
        B_start = 0
        W_start = 0

        for y in range(i, i+8):
            for x in range(j, j+8):
                if (x + y) % 2 == 0: # 그냥 두개의 경우를 나눠주기 위해서
                    if mtx[y][x] != 'B':
                        B_start += 1
                    if mtx[y][x] != 'W':
                        W_start += 1
                else:
                    if mtx[y][x] != 'W':
                        B_start += 1
                    if mtx[y][x] != 'B':
                        W_start += 1
        if min(B_start, W_start) < min_cnt:
            min_cnt = min(B_start, W_start)
print(min_cnt)
