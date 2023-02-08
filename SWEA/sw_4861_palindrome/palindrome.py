import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    mtx = []

    for i in range(n):
        row = input()
        mtx.append(row)
    for k in range(5, n + 1):
        for j in range(n):
            for i in range(n-k):
                start = i
                end = i + k
                if mtx[j][start] == mtx[j][end]:
                    while start != end and mtx[j][start] == mtx[j][end]:
                        start += 1
                        end -= 1
                    if start == end:
                        print(mtx[j][start:end+1])






