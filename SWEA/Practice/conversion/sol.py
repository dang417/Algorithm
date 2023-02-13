import sys
sys.stdin = open("input.txt")


def itoa(tc):  # 숫자형 인자를 넘겨 받음
    temp = ""
    minus = tc < 0  # 음수인지 tracking하고 있다가 return하기 전에 앞에 '-'를 붙여준다
    if minus:  # 양수처럼 처리
        tc = tc * -1

    while tc > 0:
        temp = chr(48 + (tc % 10)) + temp  # 1의 자리부터 구해 chr()함수를 이용하여 character로 바꾼다. 새로 나온 문자는 기존 문자의 앞에 위치한다
        tc = tc // 10  # 10으로 나눈 몫으로 반복한다.

    if minus:  # 음수인 경우 '-'를 앞에 연결
        temp = '-' + temp
    return temp


T = int(input())
for i in range(1, T + 1):
    tc = int(input())
    result = itoa(tc)
    print(f'#{i} {result}', type(result))
