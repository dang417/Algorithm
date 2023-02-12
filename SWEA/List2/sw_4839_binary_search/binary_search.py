# 짝을 이룬 A, B 두 사람에게 교과서에서 각자 찾을 쪽 번호를 알려주면
# 이진 탐색만으로 지정된 페이지를 먼저 펼치는 사람이 이기는 게임이다.
# 예를 들어 책이 총 400쪽이면
# 검색 구간의 왼쪽 l=1
# 오른쪽 r=400이 되고
# 중간 페이지 c= int((l+r)/2)로 계산한다.

import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1, t+1):
    p, a, b = map(int, input().split())
    A_cnt = 0
    B_cnt = 0
    start = 1
    end = p
    while start <= end:
        c = int((start+end)//2)
        if c == a:
            break
        elif c > a:
            end = c
        else:
            start = c
        A_cnt += 1

    start = 1
    end = p
    while start <= end:
        c = int((start + end) // 2)
        if c == b:
            break
        elif c > b:
            end = c
        else:
            start = c
        B_cnt += 1

    if A_cnt < B_cnt:
        print(f'#{tc} A')
    elif B_cnt < A_cnt:
        print(f'#{tc} B')
    elif B_cnt == A_cnt:
        print(f'#{tc} 0')