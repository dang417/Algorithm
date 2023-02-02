import sys
sys.stdin = open('sample_in.txt')

# 모든 버스 : A - B
# 일반 버스 : A - B 모든 정류장
# 급행 버스 : 1. A 짝수 -> 모든 짝수 정류장
#             2. A 홀수 -> 모든 홀수 정류장
# 광역 급행 : 1. A 짝수 -> 모든 4의 배수 정류장
#                A 홀수 -> 모든 3의 배수 and not 10의 배수
# 최대 몇개의 노선이 같은 정류장?
# 각 정류장에 멈추는 노선의 개수를 리스트로(idx 정류장, val 개수)

t = int(input())

for tc in range(1, t+1):
    
    n = int(input())

    cnt = [0] * 1001
    for n in range(1, n+1):
        # 버스 타입, A와 B 정류장 번호 입력
        n_list = list(map(int, input().split()))

        # 일반 버스일때
        if n_list[0] == 1:
            for i in range(n_list[1], n_list[2]+1):
                cnt[i] += 1
        # 급행 버스일때
        elif n_list[0] == 2:
            if n_list[1] % 2 == 0:
                for i in range(n_list[1], n_list[2]+1):
                    if i % 2 == 0:
                        cnt[i] += 1
            else:
                for i in range(n_list[1], n_list[2]+1):
                    if i % 2 != 0:
                        cnt[i] += 1
        # 광역 버스일때
        elif n_list[0] == 3:
            if n_list[1] % 2 == 0:
                for i in range(n_list[1], n_list[2]+1):
                    if i % 4 == 0:
                        cnt[i] += 1
            else :
                for i in range(n_list[1], n_list[2]+1+1):
                    if i % 3 == 0 and i % 10 != 0:
                        cnt[i] += 1

    max_cnt = 0

    for i in range(999):
        if cnt[i] >= max_cnt:
            max_cnt = cnt[i]

    print(f'#{tc} {max_cnt}')





