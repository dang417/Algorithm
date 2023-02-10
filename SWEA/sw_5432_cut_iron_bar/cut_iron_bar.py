# 2
# ()(((()())(())()))(())
#  |'(' '(' '(' ')(' ')' '('
#
# (((()(()()))(())()))(()())

import sys
sys.stdin = open('sample_input.txt')

t = int(input())

# 겹쳐진 쇠파이프를 한 묶음으로 만들어주는 함수
def count_iron_bar(ib):
    cnt = 0
    iron_bar = []
    pointer = i = 0
    while pointer < len(ib):
        if ib[pointer] == '(':
            cnt += 1
            pointer += 1
        elif ib[pointer] == ')':
            cnt -= 1
            pointer += 1
        if cnt == 0:
            iron_bar.append(ib[i:pointer])
            i = pointer
    return iron_bar

# 입력 받은 값에서 쇠파이프들을 묶어서 리스트화
for tc in range(1, t+1):
    ib = input()
    iron_bar = count_iron_bar(ib)
    filtered_ib = []
    # 쇠파이프 묶음 중에서 쇠파이프 없이 레이저만 있는 애들 거름
    for _ in iron_bar:
        if len(_) != 2:
            filtered_ib.append(_)

# 걸러진 쇠파이프들이 몇개로 잘라지는지 확인하기
    rlt = []
    bars = 0
    for i in filtered_ib:
        j = 0
        while j < len(i):
            if i[j:j + 2] != '()':
                if i[j] == '(':
                    bars += 1
            if i[j] == ')':
                rlt.append(1)
                bars -= 1
            if i[j:j+2] == '()':
                rlt.append(bars)
                j += 1
            j += 1

    print(f'#{tc}', sum(rlt))








