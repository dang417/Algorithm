import sys
sys.stdin = open('input1.txt')

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    num = input()
    max_cnt = 0
    cnt = 1

    for i in range(n-1):
        if num[i] == '1' and num[i+1] == '1':
            cnt +=1 
        elif num[i] == '1' and num[i+1] == '0':
            if cnt >= max_cnt:
                max_cnt = cnt
            cnt = 1

    if cnt >= max_cnt:
        max_cnt = cnt

    if n == 1 and num[0] == '0':
        max_cnt = 0

    print(f'#{tc} {max_cnt}')

'''

'''