import sys
sys.stdin = open('input.txt')
while True:
    tmp = input()
    if tmp == 'end':
        break
    cnt = 0
    if tmp[0] == tmp[4] == tmp[8]:
        cnt += 1
    if tmp[2] == tmp[4] == tmp[6]:
        cnt += 1
    for i in range(3):
        if tmp[i*3] == tmp[(i*3)+1] == tmp[(i*3)+2]:
            cnt += 1
        if tmp[i] == tmp[i+3] == tmp[i+6]:
            cnt += 1

    if cnt >= 2:
        print('invalid')
    else:
        print('valid')