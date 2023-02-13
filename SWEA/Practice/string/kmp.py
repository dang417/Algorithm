import sys
sys.stdin = open('input.txt', encoding='utf-8')

# 패턴 내의 패턴이 존재하는지 그리고 그 정보를 담기위한 리스트 만드는 함수
def make_lps(pattern):
    # 중계 리스트
    lps = [0] * len(pattern)

    # lps의 각 인덱스에 이전 패턴정보 담기위한 인덱스
    lps_idx = 0
    for i in range(1, len(pattern)):
        # 이전번 글자와 지금 조사하는 글자가 같다면
        if pattern[lps_idx] == pattern[i]:
            lps[i] = lps_idx + 1
            lps_idx += 1
        else:
            # 다를때 0으로 초기화 시켜서 패턴의 0번째와 다시비교
            lps_idx = 0
            if pattern[i] == pattern[lps_idx]:
                lps[i] = lps_idx + 1
                lps_idx += 1
    return lps


def KMP(pattern, target):
    lps = make_lps(pattern)
    # 조사 시작은 Brute Force 방법과 동일하게 시작
    p_idx = 0
    t_idx = 0
    count = 0
    while t_idx < len(target):
        if pattern[p_idx] == target[t_idx]:
            t_idx += 1
            p_idx += 1
        else:
            if p_idx == 0:
                t_idx += 1
            else:
                p_idx = lps[p_idx - 1]
        if p_idx == len(pattern):
            count += 1
            p_idx = 0
    return count




for _ in range(10):
    tc = int(input())
    pattern = input()
    target = input()

    print(make_lps(pattern))