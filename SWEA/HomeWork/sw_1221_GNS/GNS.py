import sys
sys.stdin = open('GNS_test_input.txt')

t = int(input())

for _ in range(t):
    tc, n = input().split()
    n = int(n)
    # 딕셔너리에 각 외계행성 숫자에 대응하는 숫자 저장
    num_dict = {"ZRO" : 0,
                "ONE" : 1,
                "TWO" : 2,
                "THR" : 3,
                "FOR" : 4,
                "FIV" : 5,
                "SIX" : 6,
                "SVN" : 7,
                "EGT" : 8,
                "NIN" : 9
                }
    # 카운팅 정렬 하겠습니다
    # 카운트를 저장할 리스트
    C = [0] * 10
    # 입력받은 숫자들의 동일한 인덱스에 dict 에서 찾은 밸류값을 저장할 임시 리스트
    tmp = [0] * n
    # 그 임시 리스트에서 카운트 한 개수를 기반으로 결과를 저장할 result 리스트
    rlt = [0] * n
    # 입력받은 숫자들을 리스트 형태로 저장
    num_list = list(input().split())
    # 리스트의 숫자들에 대해 dict에서 밸류를 찾아 같은 인덱스로 임시 리스트에 저장
    for i in range(n):
        tmp[i] = num_dict[num_list[i]]
    # 임시 리스트의 값들을 C의 인덱스로 활용하여 임시 리스트를 순회하며 개수를 카운트(+=1)
    for value in tmp:
        C[value] += 1
    # 카운트의 개수들이 누적되어야 하므로 순회하며 이전의 값들을 뒤 값에 계속 더 해줌
    for i in range(1, 10):
        C[i] += C[i-1]
    # 그 개수를 인덱스 값으로 하는 rlt의 주소에 해당하는 외계 숫자를 저장
    # 하며 숫자의 개수를 한개 뺌
    for num in num_list:
        rlt[C[num_dict[num]]-1] = num
        C[num_dict[num]] -= 1
    # 이렇게 하면 700개의 ZRO가 0~699까지 정렬되며 입력
    # 이후의 숫자들도 마찬가지
    print(tc)
    print(*rlt)





