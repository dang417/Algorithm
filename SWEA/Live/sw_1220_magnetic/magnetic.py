import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(n)]
    stack = []
    rlt = 0

    for i in range(n):
        for j in range(i, n):
            table[i][j], table[j][i] = table[j][i], table[i][j]

    for i in range(n):
        string = ''
        for num in table[i]:
            if num != 0:
                string += str(num)
        for j in range(len(string)-1):
            if string[j] == '1' and string[j+1] == '2':
                rlt += 1

    print(f'#{tc}', rlt)