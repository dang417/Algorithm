import sys
sys.stdin = open('test_input.txt', encoding='utf-8')

# for test_case in range(10):
#     tc = int(input())
#     pattern = input()
#     target_string = input()
#     p = len(pattern)
#     t = len(target_string)
#     # 조사 하려고 하는 두 대상의 조사 대상을 내가 직접 컨트롤 하는
#     # 인덱스로 조절하면서 비교하겠다.
#     p_idx = 0
#     t_idx = 0
#     cnt = 0
#     # 패턴이 문장에서 몇 번 나오는지 세려고
#     # 조사를 할건데 언제까지 순회 하는가
#     # 최종 결과값
#     while t_idx < t:
#         # # 모든 패턴에 대해 조사를 마쳤다면
#         # if p_idx == p:
#         #     cnt += 1
#         #     p_idx = 0
#         if pattern[p_idx] == target_string[t_idx]:
#             p_idx += 1
#             t_idx += 1
#
#         if target_string[t_idx] != pattern[p_idx]:
#             t_idx = t_idx - p_idx
#             t_idx += 1
#             p_idx = -1
#             # 왜 0이 아니라 -1 인가
#             # p_idx는 모든 상황에 대해서 항상 증가할 것이기 때문에
#             # 0으로 설정하면 한 번 틀리면 처음부터 조사를 하지 않고 끝부터 조사함
#         # 두 값이 같으면 idx를 증가 시킴
#     print(cnt)

# for 문으로 찾기

for _ in range(10):
    tc = int(input())
    pattern = input()
    target = input()
    cnt = 0
    for t_idx in range(len(target) - len(pattern)+1):
        for p_idx in range(len(pattern)):
            if pattern[p_idx] != target[t_idx + p_idx]:
                break
        else:
            cnt += 1
    print(f'#{tc}', cnt)
