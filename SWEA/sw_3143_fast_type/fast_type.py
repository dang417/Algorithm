import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1, t+1):
    A, B = input().split()

    A_list = list(A)
    B_list = list(B)

    a = 0
    b = 0

    while a != len(A_list):
        if A_list[a] == B_list[b]:
            a += 1
            b += 1
        else:
            a = a - b + 1
            b = 0

        if b == len(B):
            A_list[a-b:a] = '~'
            a = a - b + 1
            b = 0
    print(f'#{tc}', len(A_list))

    # if B in A:
    #     A = A.replace(B, 'o')
    # print(f'#{tc}', len(A))
    # # 글자 패턴이 일치하면 += 1
    # # 일치 하지 않으면 += 1

    # 탐색으로 일치하면 그 값들을 변경해주자
