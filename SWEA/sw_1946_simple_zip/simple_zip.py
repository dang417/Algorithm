import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    print(f'#{tc}')
    n = int(input())
    char_num = []
    tmp = []
    cnt = 0
    for i in range(n):
        char_num.append(input().split())
    for j in range(len(char_num)):
        for k in range(int(char_num[j][1])):
            tmp.append(char_num[j][0])
    for chars in tmp:  
        print(chars, end='')
        cnt += 1
        if cnt == 10:
            print()
            cnt = 0
    print()

