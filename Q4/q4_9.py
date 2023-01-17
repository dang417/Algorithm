import sys

c = int(input())

for i in range(c) :
    case = list(map(int,sys.stdin.readline().split()))
    avg = sum(case[1:])/case[0]

    cnt = 0
    for i in case[1:] :
        if i > avg :
            cnt += 1

    per = (cnt/case[0])*100
    print('%.3f' %per + '%')
    #%.3f : per의 소수점 3번째 자리까지 출력한다