import sys
sys.stdin = open('input.txt')

for t in range(1):
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(n)]
    stack = []
    rlt = 0
    for i in range(100):
        for j in range(1, 100):
            table[i][j], table[j][i] = table[j][i], table[i][j]
    for i in range(100):
        tmp = []
        for j in range(100):
            if table[i][j] == 1 and (2 in table[i][j:]):
                if tmp and tmp[-1] == 1:
                    continue
                tmp.append(1)
            elif tmp and table[i][j] == 2:
                if tmp and tmp[-1] == 2:
                    continue
                tmp.append(2)
        print(len(tmp) // 2)
        rlt += len(tmp) // 2
    for i in range(100):
        for j in range(98):
            if table[i][j+1] == 1 and table[i][j] ==  table[i][j+2] == 2:
                rlt -= 1
            elif table[i][j+1] == 2 and table[i][j] == table[i][j+2] == 1:
                rlt -=1
    print(rlt)