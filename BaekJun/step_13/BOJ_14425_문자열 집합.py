import sys
input = sys.stdin.readline
n, m = map(int,input().split())
n_set = {input() for _ in range(n)}
m_list = [input() for _ in range(m)]
cnt = 0
for i in m_list:
    if i in n_set:
        cnt += 1
print(cnt)