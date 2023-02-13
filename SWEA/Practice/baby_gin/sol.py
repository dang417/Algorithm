import sys
sys.stdin = open('input.txt')


def check(n):
    flag = 0                    # triplet or run이 몇번 나왔는지 체크
    while True:                 # 아래 조건을 만족할때까지 반복
        if visited[n] >= 3:     # n번이 3번 이상 나왔다면 triplet
            flag += 1           # 횟수 증가
            visited[n] -= 3     # 한번 체크 했으므로 해당 수 제거
        # n이 7이하일때만 run 검증 (index를 넘지 않도록)
        elif n <= 7 and visited[n] >= 1 and visited[n + 1] >= 1 and visited[n + 2] >= 1:
            flag += 1
            visited[n] -= 1     # n번 부터 연달아 있는 3개의 수 체크
            visited[n + 1] -= 1
            visited[n + 2] -= 1
        else:                   # 위 조건을 모두 만족하지 못하는경우 발생시
            return flag         # 지금까지 기록한 triplet, run의 개수를 반환하고 종료


T = int(input())

for tc in range(1, T+1):
    numbers = list(map(int, input()))

    visited = [0] * 10          # 0-9번 수가 몇번 나왔는지 체크하기 위한 리스트
    for i in range(6):
        visited[numbers[i]] += 1

    result = 0
    for n in range(10):         # 모든 수에 대해서 triplet or run 검증
        result += check(n)      # 반환된 값 누적

    print(f'#{tc}', end=' ')    # 누적된 결과에 따라 정답 출력
    print(1) if result >= 2 else print(0)