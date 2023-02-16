def solution(arr, K, result):
    # 부분집합의 합이 10인 경우를 찾고 있다.
    if result != 10:
        return
    for i in range(1, K+1):
        if arr[i]:
            print(data[i], end = ' ')
    print()

def make_ncandidates(arr, K, N, c):
    c[0] = True     # 쓰겠다
    c[1] = False    # 안쓰겠다
    return 2        # 생각할 수 있는 경우의 수

def backtracking(arr, K, N, result):
    # 만약 result 가 10을 넘어가면 멈추고 다시 백트래킹
    if result > 10:
        return
    # 총합 계산은 result로 진행
    # 후보군 목록
    c = [0] * 2     # 부분집합 원소 쓴다/ 안쓴다만 구분 하기 때문에 2개만 있어도 됨
    # 언제까지 조사 할건지?
    # 현재 조사하는 위치가 최대 조사 상황에 도달할때 까지
    if K == N:
        solution(arr, K, result)    # 값을 도출하는 함수 실행
    else:
        K += 1
        # 아직 사용해야 하는 원소들이 남았다면,
        # 사용할 원소 인덱스 1 증가
        # 내가 해당 원소를 쓸/말 결정하는 경우의 수 2개
        # 배열, 지금까지 사용한 원소 인덱스, 최대 원소 개수, 후보군 목록
        ncandidates = make_ncandidates(arr, K, N, c)
        for i in range(ncandidates):    # 후보군 수 만큼 변
            arr[K] = c[i]
            if arr[K]:  # K번째 원소 쓰기로 했으면
            # 총합에 원본 데이터의 K번째 원소의 값을 더해준다
                backtracking(arr, K, N, result + data[K])
            else:
                # 지금 K번째 원소를 쓰지는 않지만,
                # 다음 조사는 해야 한다, 대신 안쓸꺼니까 총합에 안더하기
                backtracking(arr, K, N, result)


# 유망성 조사를 위한 변수
MAXCANDIDATES = 12 # 최대 후보군 수, 쓸 건지 안 쓸 건지를 적어놓기 위한 변수
NMAX = 12 # 최대 원소 수

data = list(range(11))
arr = [0] * NMAX

# 조사를 시작
# 체크할 배열, 시작점, 종료지점, 총합
backtracking(arr, 0, 10, 0)
