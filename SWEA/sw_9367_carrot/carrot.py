import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    cnt = 1
    cnt_list = []
    n = int(input()) # 5
    carrot_list = list(map(int, input().split())) #1 2 3 4(3) 5(4)  12345670~4

    for i in range(n-1): #range(4) = 0 1 2 3
        if carrot_list[i] < carrot_list[i+1]: #if list[4] < list[5] index error
            cnt += 1
        else:
            cnt_list.append(cnt)
            cnt = 1

    cnt_list.append(cnt)

    print(f'#{tc} {max(cnt_list)}')




