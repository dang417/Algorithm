import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    cnt = 1
    cnt_list = []
    n = int(input())
    carrot_list = list(map(int, input().split()))

    for i in range(n-1):
        if carrot_list[i] < carrot_list[i+1]:
            cnt += 1
        else:
            cnt_list.append(cnt)
            cnt = 1
    else:
        cnt_list.append(cnt)

    print(f'#{tc} {max(cnt_list)}')




