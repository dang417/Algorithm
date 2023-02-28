import sys
sys.stdin = open('s_input.txt')

t = int(input())

for tc in range(1, t+1):
    words = [list(input()) for _ in range(5)]
    rlt = ''
    for j in range(15):
        for i in range(5):
            if len(words[i]) > j:
                rlt += words[i][j]

    print(f'#{tc}', rlt)