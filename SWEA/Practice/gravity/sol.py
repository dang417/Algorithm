import sys
sys.stdin = open('input.txt')

# 전체 테스트 케이스 수
N = int(input())

# N번 만큼 순회하면서 각 TC에 대한 풀이 진행
for tc in range(1, N+1):
    # 상자들이 담겨있는 칸의 개수
    A = int(input())
    # 각 상자들의 높이가 담겨있는 리스트
    # 공백을 기준으로 나눠서 입력받은 문자열의 각 값들
    # 하나하나를 int로 변환한 다음 리스트에 담아서 반환
    numbers = list(map(int, input().split()))
    # print(tc, A, numbers)

    # 최종 결괏값
    result = 0
    # 모든 상황에 대한 낙찻값을 위해 전체 순회
    for i in range(A):
        # i번쨰 상자가 떨어질 수 있는 최대
        # 방해를 받지 않았을 떄의 최대
        # 전체 길이 - 내 위치 + 1
        max_h = len(numbers) - (i+1)

        # 내 다음으로 오는 상자들 중에 나보다 크거나 같은 값들
        for j in range(i+1, len(numbers)):
            # i보다 j가 크거나 같은 값
            # 내 높이 보다 j번쨰 위치가 크거나 같은 값
            if numbers[i] <= numbers[j]:
                max_h -= 1

        # 지금 막 낙차값 구한 그 max_h가 최종 결괏값보다 크다면
        if result < max_h:
            result = max_h

    print(f'#{tc} {result}')
