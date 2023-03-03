import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    n, m, k = map(int, input().split())
    people = sorted(list(map(int, input().split())))
    time = m
    cake_cnt = k
    A = True
    while A:
        for i in range(k):
            if people[i] >= time:
                if people[i] == people[-1]:
                    people = []
                    break
                pass
            else:
                print(f'#{tc} Impossible')
                A = False
                break
        else:
            people = people[k:]
        if not people:
            print(f'#{tc} Possible')
            break
        time += m