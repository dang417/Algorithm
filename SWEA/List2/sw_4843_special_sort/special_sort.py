# N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.
# 10 1 9 2 8 3 7 4 6 5

import sys
sys.stdin = open('sample_input.txt')
# 먼저 리스트를 정렬한 후(선택 정렬)
# 리스트를 반(left, right) 로 나눈다
# left는 앞에서부터 right는 뒤에서부터 순회하며
# rlt 리스트에 하나씩 추가한다
# 이때 출력값은 10개 까지만 인것에 주의

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    raw_list = list(map(int, input().split()))
    rlt = []
    
# 리스트를 정렬하기 위해
# 포인터 i 를 정하고 minidx로 지정한 후 i+1 부터 j로 순회하며
# 만약 minidx의 데이터가 j의 데이터보다 크다면
# 둘의 자리를 바꿔준다
# 반복 후에 정렬 완료

    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if raw_list[i] > raw_list[j]:
                min_idx = j
                raw_list[i], raw_list[min_idx] = raw_list[min_idx], raw_list[i]

# 리스트의 중간 idx를 찾은 후
# 슬라이싱으로 left, right 지정

    mid = len(raw_list)//2
    left = raw_list[:mid]
    right = raw_list[mid:]
# 두개의 포인터를 활용해 (i, j의 값을 초기화 해주어 상관X)

    k = 0
    l = (n//2) - 1

# 10개의 값 까지만
# right는 뒤쪽에서 부터(큰 값부터) left는 앞쪽에서부터(작은 값 부터) rlt에 저장

    for k in range(5):
        rlt.append(right[l])
        l -= 1
        rlt.append(left[k])
        k += 1

# 각 tc에 대하여 출력

    print(f'#{tc}',*rlt)

