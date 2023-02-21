import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1, t+1):
    word_arr = [list(input()) for _ in range(5)]
    max_len = 0
    for i in range(5):
        if len(word_arr[i]) >= max_len:
            max_len = len(word_arr[i])
    rlt = ''
    j = 0
    while max_len > j:
        for i in range(5):
            if len(word_arr[i]) > j:
                rlt += word_arr[i][j]
        j += 1

    print(f'#{tc}', rlt)