
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

for i in range(m-8):
    sliced_mtx = []
    for j in range(n-8):
        sliced_row = mtx[j]
        sliced_mtx.append(sliced_row[i:i+8])
    print(sliced_mtx)